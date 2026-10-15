/**
 * Teaching model of documented Genesys Cloud ACD behavior.
 * It is not the production router. See the Resource Center articles
 * linked from the routing lessons.
 */

export function conversationRank(interaction) {
  return interaction.arrivedMs - interaction.priority * 60000;
}

export function decide(input) {
  const trace = [];
  const waiting = [...input.interactions].sort((a, b) => {
    if (input.scoring === "priority") {
      if (b.priority !== a.priority) return b.priority - a.priority;
      return a.arrivedMs - b.arrivedMs;
    }
    return conversationRank(a) - conversationRank(b);
  });
  const interaction = waiting[0];
  if (!interaction) return { winner: null, trace: ["No interaction is waiting."] };
  trace.push(`Selected interaction "${interaction.id}" with ${input.scoring === "priority" ? "priority score" : "conversation score"}.`);

  const elapsed = input.elapsedMs || 0;
  const rings = input.rings && input.rings.length ? input.rings : [{ delayMs: 0, remove: [] }];
  let activeRing = 0;
  let consumed = 0;
  for (let i = 0; i < rings.length - 1; i += 1) {
    const delay = rings[i].delayMs ?? 0;
    if (elapsed >= consumed + delay) {
      consumed += delay;
      activeRing = i + 1;
    } else break;
  }
  const required = new Set(interaction.skills);
  for (let i = 1; i <= activeRing; i += 1) {
    (rings[i].remove || []).forEach((skill) => required.delete(skill));
  }
  trace.push(`Bullseye ring ${activeRing + 1} of ${rings.length}. Required skills: ${[...required].join(", ") || "(none)"}.`);

  const eligible = input.agents.filter((agent) => {
    if (!agent.onQueue) {
      trace.push(`${agent.name} is not On Queue.`);
      return false;
    }
    if (agent.utilized) {
      trace.push(`${agent.name} is at utilization and is skipped.`);
      return false;
    }
    if (input.evaluation !== "disregard") {
      const missing = [...required].filter((skill) => !agent.skills[skill]);
      if (missing.length && !(input.prefer && agent.preferred)) {
        trace.push(`${agent.name} is missing ${missing.join(", ")}.`);
        return false;
      }
      if (missing.length && agent.preferred) {
        trace.push(`${agent.name} is preferred and is eligible even without ${missing.join(", ")}.`);
      }
    }
    return true;
  });

  if (!eligible.length) {
    trace.push("No agent can take this interaction on the active ring.");
    return { winner: null, ring: activeRing + 1, required: [...required], trace };
  }

  let pool = eligible;
  if (input.prefer) {
    const preferred = eligible.filter((agent) => agent.preferred);
    if (preferred.length) {
      pool = preferred;
      trace.push("Preferred agents are considered first, including agents who lack a required skill.");
    } else {
      trace.push("No preferred agent is eligible on this ring.");
    }
  } else if (input.evaluation === "best") {
    pool = [...eligible].sort((a, b) => b.idleMs - a.idleMs).slice(0, 100);
    trace.push(`Best available skills considers the ${pool.length} longest-idle matching agent${pool.length === 1 ? "" : "s"} (cap 100).`);
  }

  const useProficiency = input.evaluation === "best" && !(input.prefer && pool.some((agent) => agent.preferred));
  pool.sort((a, b) => {
    if (useProficiency) {
      const diff = avgProf(b, required) - avgProf(a, required);
      if (diff) return diff;
    }
    return b.idleMs - a.idleMs;
  });
  const winner = pool[0];
  trace.push(`${winner.name} wins${input.evaluation === "best" ? " on average proficiency, then idle time" : " as the longest idle match"}.`);
  return { winner, ring: activeRing + 1, required: [...required], trace };
}

function avgProf(agent, required) {
  const skills = [...required];
  if (!skills.length) return 0;
  const total = skills.reduce((sum, skill) => sum + (agent.skills[skill] || 0), 0);
  return total / skills.length;
}
