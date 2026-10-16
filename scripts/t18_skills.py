from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "skills",
    "title": "Skills and ACD",
    "kicker": "Chapter",
    "accent": 1,
    "summary": "How Genesys Cloud matches a skill request to an agent, from the ACD idea through filters, rings, and direct routing.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "k-what", "ACD is the match, and skills are one way to make it", "Foundation", 12,
    "Wikipedia describes an ACD as a distributor. Genesys Cloud puts that job on the queue’s routing method.",
    [
        "The Wikipedia article describes an automatic call distributor as a system that answers and distributes incoming calls, and it describes skills-based routing as routing by an operator’s knowledge. Genesys Cloud’s evaluation article is more specific: ACD uses the queue’s routing method to match interactions and agents. When the method is skills-based, the evaluation method decides how a skill request is processed. A customer can request skills from the IVR.",
        "The queue settings article lists five routing methods: standard, predictive, bullseye, preferred agent, and conditional group. The advanced routing overview describes those and also describes direct routing, which sends the interaction to a dedicated person instead of the next available agent. Direct routing is not a sixth choice in that five-method list. The ACD track in this lab drills the five methods. This chapter adds the filter, the ring-count conflict, and direct routing.",
    ],
    cites("wiki-acd", "evaluation", "routing", "routing-settings"),
    fig("The queue method decides the match. Skills are an input, not the whole ACD.", [
        ("in", "Interaction", "phone", 14, 40),
        ("q", "Queue method", "queue", 48, 28),
        ("ev", "Evaluation", "architect", 48, 68),
        ("ag", "Agent", "agent", 82, 40),
    ], [("in", "q"), ("q", "ev"), ("ev", "ag")]),
    "Name the method before you name a skill",
    [
        ("Idea", "ACD", "Distribute the contact", "Wikipedia’s general description.", "Not a Genesys setting"),
        ("Queue", "Method", "Five on the settings page", "Standard is the default.", "Direct routing is separate"),
        ("Skill", "Request", "From the IVR or the flow", "Evaluation decides what “has the skills” means.", "Disregard skills ignores them"),
        ("Lab", "Track", "The ACD track drills the five", "This chapter continues past that list.", "Open both"),
    ],
    [
        q("On the evaluation article, Genesys Cloud ACD matches interactions by:", "The queue’s routing method", ["The trunk transport", "The exam catalog", "A Wikipedia distribution list"], "Skills matter when that method is skills-based."),
        q("The settings article’s routing-method list has:", "Five methods, and standard is the default", ["Direct routing as method six", "Only bullseye", "Only skills"], "Direct routing is described on the advanced routing overview, not in that five-item list."),
        q("A skill request can come from:", "The IVR, as the evaluation article says", ["The fair-use price table", "An RFC address range", "The certification webcam rule"], "The evaluation method then processes it."),
        q("Wikipedia’s skills-based routing, as that page describes it, is:", "Routing by an operator’s knowledge", ["A Genesys ring cap", "A token allotment", "A SIP response code"], "Use it as the general idea. Use the Genesys article for the product."),
        q("Disregard skills is:", "An evaluation method, not a wipe of the agent profile", ["The deletion of every skill in the org", "Direct routing", "A forecast method"], "The settings article lists it next to all-skills and best-available."),
        q("This chapter sits next to the ACD track because:", "The track drills the five methods, and this chapter continues into filters and direct routing", ["It replaces the queue", "It signs in to an organization", "It sets a price"], "Nothing here calls an API."),
    ],
    [("ACD", "The queue’s routing method."), ("Five", "Standard, predictive, bullseye, preferred, conditional."), ("Direct", "Described separately."), ("Skills", "Processed by the evaluation method.")],
    "Separate the idea from the setting",
    ["Write one sentence from the Wikipedia description.", "Name the five methods from the settings article.", "Say where direct routing is described.", "Say which evaluation method ignores skills."],
    "The five names and the direct-routing distinction are both written down.",
    ("Sixth method", "A design calls direct routing “standard routing method number six” on the queue.", "The settings list has five methods. Direct routing has its own overview.", "The lists were merged.", "Keep direct routing on its own row and pick one of the five for the queue method."),
))

add(lesson(
    "k-eval", "Three evaluation methods, and a seven-day lookback", "Foundation", 13,
    "All skills matching, best available skills, and disregard skills do different jobs. Proficiency covers ACD skills and language skills together.",
    [
        "All skills matching selects the agent who has every required skill and the longest time since the last interaction. It does not use the skill rating. Best available skills considers the 100 agents with the longest time since the last interaction, keeps those who have every required skill, and assigns the interaction to the highest average proficiency. Equal averages go to the longest idle of that group. Disregard skills, next agent, selects the longest idle agent and does not consider skills.",
        "The evaluation article says Genesys Cloud looks back 7 days when it chooses the next agent. An agent who has not been on queue for more than 7 days is not ranked by an older last-handled time. Proficiency scores are considered for ACD skills and language skills together. Status changes and on-queue behavior do not change that idle priority. If the agent belongs to several queues, idle time counts across those queues, not only the queue being evaluated.",
    ],
    cites("evaluation", "bullseye"),
    fig("All-skills sorts by idle time. Best-available sorts by proficiency inside a window of 100.", [
        ("all", "All skills", "agent", 18, 40),
        ("best", "Best of 100", "agent", 50, 40),
        ("none", "Disregard", "queue", 82, 40),
    ], [("all", "best"), ("best", "none")]),
    "Score the same three agents three ways",
    [
        ("All skills", "Pool", "Every required skill", "Then longest idle.", "Rating is ignored"),
        ("Best", "Window", "100 longest idle", "Then highest average proficiency.", "Idle breaks a tie"),
        ("Disregard", "Anyone", "Longest idle", "Skills do not filter.", "Rings mean less"),
        ("Lookback", "7 days", "Older idle is dropped", "A quiet agent is not infinitely idle.", "Language skills share the average"),
    ],
    [
        q("All skills matching ignores:", "The skill rating", ["Whether the agent has every skill", "Idle time", "The 7-day lookback"], "It sorts the full-skill agents by time since last interaction."),
        q("Best available skills starts with:", "The 100 agents with the longest time since last interaction", ["Every agent in the organization", "Only preferred agents", "Only language skills"], "Then it averages proficiency among those who have the required skills."),
        q("A proficiency tie in best available skills goes to:", "The longest time since last interaction", ["The shortest name", "The home division", "The lowest license"], "The evaluation article states that tie-break."),
        q("The lookback for last-handled time is:", "7 days", ["7 minutes", "30 days", "All history"], "An agent idle for more than 7 days is not treated as older than one idle for 5."),
        q("Proficiency averages include:", "ACD skills and language skills together", ["Only the queue name", "Only wrap-up codes", "Only the division"], "The evaluation article says both."),
        q("Idle time for an agent on two queues is:", "Calculated across the agent’s queues", ["Only the queue on the screen", "Reset by a status change", "Ignored under all skills matching"], "The note says it is not restricted to the queue under evaluation."),
    ],
    [("All", "Longest idle with every skill."), ("Best", "100 longest idle, then average proficiency."), ("Disregard", "Longest idle, skills ignored."), ("7 days", "Older last-handled time drops out.")],
    "Write the winner for one interaction",
    ["List the required skills.", "Pick all-skills or best-available.", "Name the winner and the reason.", "Say what changes if the winner has been off queue for 10 days."],
    "The winner follows one method, and the 7-day note is included.",
    ("Rating surprise", "The highest-rated bilingual agent waits while a lower-rated peer takes the call.", "Evaluation: all skills matching. Both have the skills.", "All skills matching does not sort by rating.", "Switch to best available skills if the rating is the policy, and retest."),
))

add(lesson(
    "k-rings", "Bullseye widens the pool in two documented ways", "Core", 14,
    "One way adds skill-expression groups. The other removes skills. The ring count is not the same sentence on every page.",
    [
        "The bullseye overview describes expansion as concentric rings. Option 1 adds agents from groups on the next ring, and it tells you to use skill expression groups with the same skills at different proficiencies so WEM forecasting and scheduling can keep the planning group intact. Agents who lack the skills are not evaluated. Option 2 removes skills from the evaluation on the next ring. The skills stay on the interaction. Removal works best with all skills matching or best available skills. The settings article caps removals at 50 skills on one ring, and the delay is from 2 seconds to 259,200 seconds (72 hours).",
        "The same settings article first says define up to five rings, then in the skill-removal steps says add rings up to six. Preferred-agent rings on that page also say up to six. The advanced routing overview says create up to six rings. The bullseye examples expand through ring 6. This lab will not pick a single cap those pages do not share. Count the rings the queue UI offers before you design a sixth. Inner-ring agents keep priority after an outer ring opens. Preferred agents are considered even without the required skills.",
    ],
    cites("bullseye", "routing-settings", "routing"),
    fig("Option 1 keeps the skill and lowers proficiency. Option 2 removes a skill on the way out.", [
        ("r1", "Ring 1", "agent", 22, 36),
        ("opt", "Two options", "architect", 52, 36),
        ("wem", "WEM groups", "wem", 82, 22),
        ("drop", "Remove skill", "queue", 82, 68),
    ], [("r1", "opt"), ("opt", "wem"), ("opt", "drop")]),
    "Choose an expansion style before you count rings",
    [
        ("WEM", "Option 1", "Same skills, lower proficiency", "Skill expression groups.", "Planning group stays intact"),
        ("Relax", "Option 2", "Skills to remove on exit", "Up to 50 on a ring.", "Best with strict evaluation"),
        ("Time", "Delay", "2 seconds to 72 hours", "The ring does not skip the wait.", "259,200 seconds"),
        ("Count", "Confirm", "Five in the first instruction, six later", "Read the control you will click.", "Do not memorize one number"),
    ],
    [
        q("Option 1 stays compatible with WEM forecasting by:", "Skill expression groups that share the skills at different proficiencies", ["Removing every skill", "Disregard skills", "A blank forecast"], "The bullseye overview and the settings article both say this."),
        q("Option 2 removes a skill from:", "The evaluation on the next ring, not from the interaction", ["The agent’s profile permanently", "The organization", "The forecast"], "The overview says the skills remain on the interaction."),
        q("The removal cap on one ring is:", "50 skills", ["5 skills", "6 skills", "500 skills"], "The settings article states 50."),
        q("The ring delay range on the settings article is:", "2 seconds to 259,200 seconds", ["0 to 30 seconds", "7 days to 30 days", "15, 30, or 60 minutes"], "259,200 seconds is 72 hours. The minute values are forecast granularity."),
        q("The bullseye ring cap across the pages opened for this lesson is:", "Not one number: the first instruction says five, later steps and the overview say six", ["Always three", "Always 50", "Unlimited"], "Confirm the rings the queue offers."),
        q("After ring 2 opens, a free ring 1 agent:", "Still has priority over ring 2", ["Is removed from the queue", "Loses the skill", "Becomes a forecast"], "The overview’s walkthrough says inner rings keep priority."),
    ],
    [("Option 1", "Same skills, lower proficiency."), ("Option 2", "Remove up to 50 skills."), ("Delay", "2 seconds to 72 hours."), ("Cap", "Five and six both appear. Confirm.")],
    "Write one ring plan",
    ["Pick option 1 or option 2.", "Write the delay.", "Write the proficiency or the skill you remove.", "Write “confirm the ring count in the queue” instead of a single cap."],
    "The plan names one expansion style and does not invent a ring cap.",
    ("Sixth ring on a slide", "The design shows six rings because the overview says six, and the queue screen the team captured stops at five.", "Both sentences exist.", "The slide picked one page.", "Match the slide to the control that org actually offers, and cite the sentence you used."),
    "Opened in 2026-10: the settings article says define up to five rings and, later, up to six. The advanced routing overview says create up to six rings.",
))

add(lesson(
    "k-filter", "A skill expression filter replaces the queue’s skill list", "Core", 13,
    "It works for standard and predictive routing when evaluation is All skills matching. Other methods ignore it.",
    [
        "The evaluation article describes an optional ACD skill expression filter. You define a combination of skills and proficiencies in Architect, or supply it through the API, and Genesys Cloud applies it when the conversation transfers to a queue or while it waits. The filter is used instead of the ACD skills and language skills configured on the queue, and only when the routing method is standard or predictive and the evaluation method is All skills matching.",
        "The same article says the filter does not work with preferred agent routing, last agent routing, direct routing, or bullseye routing. If no filter is defined, or the filter is invalid, routing uses the queue’s method and skill configuration. A filter is invalid when the expression has a syntax error, a skill or language skill cannot be resolved, or the expression cannot be evaluated at runtime.",
    ],
    cites("evaluation", "routing", "architect"),
    fig("A valid filter narrows the pool. An invalid filter falls back to the queue.", [
        ("arch", "Expression", "architect", 16, 40),
        ("q", "All skills", "queue", 48, 40),
        ("bad", "Invalid", "phone", 78, 22),
        ("ok", "Queue skills", "agent", 78, 68),
    ], [("arch", "q"), ("bad", "ok")]),
    "Decide whether the filter is even allowed",
    [
        ("Method", "Standard or predictive", "Required", "Bullseye does not use the filter.", "Neither does direct routing"),
        ("Evaluation", "All skills matching", "Required", "Best available and disregard are not the documented pair.", "Check the queue"),
        ("Source", "Architect or API", "The expression", "It replaces the queue skill list when valid.", "Language skills included"),
        ("Failure", "Invalid", "Syntax or unknown skill", "The queue configuration is used.", "Do not assume a silent empty pool"),
    ],
    [
        q("A skill expression filter is applied when the queue uses:", "Standard or predictive routing, and All skills matching", ["Bullseye and disregard skills", "Preferred agent routing", "Direct routing"], "The evaluation article limits the pair."),
        q("When the filter is valid, Genesys Cloud evaluates:", "The filter, instead of the queue’s ACD and language skills", ["Only the queue skills, and ignores the filter", "Only preferred agents", "A forecast"], "That replacement is the point of the filter."),
        q("The filter does not work with:", "Preferred agent, last agent, direct, or bullseye routing", ["Standard routing", "All skills matching", "An Architect transfer"], "The article lists those four exclusions."),
        q("An expression that names a skill the org cannot resolve is:", "Invalid, so the queue’s own skill configuration is used", ["A successful empty match", "A new bullseye ring", "A published bot"], "Invalid also includes syntax errors and a runtime evaluation failure."),
        q("You can supply the filter from:", "Architect, and also the API", ["Only a cheat sheet", "Only a forecast CSV", "Only the Edge"], "The article names both."),
        q("With no filter defined, routing uses:", "The routing method and skills on the queue", ["Disregard skills automatically", "Direct routing", "The long-term forecast"], "The filter is optional."),
    ],
    [("Pair", "Standard or predictive, plus all skills matching."), ("Replaces", "The queue’s ACD and language skills."), ("Excludes", "Preferred, last agent, direct, bullseye."), ("Invalid", "Fall back to the queue.")],
    "Accept or reject three filters",
    ["A standard queue with all skills matching.", "A bullseye queue.", "An expression that names a missing skill.", "Write the fallback for the third."],
    "Only the first filter is eligible, and the third names the fallback.",
    ("Silent filter", "Bullseye is on, and an Architect expression was added so VIP language would apply. The queue still uses its ring skills.", "The article says the filter does not work with bullseye.", "The expression was treated as universal.", "Remove it from the bullseye design or change the queue method to a pair the filter supports."),
))

add(lesson(
    "k-direct", "Direct routing still uses a queue", "Advanced", 13,
    "The customer reaches a dedicated person. Wrap-up still exists, because the interaction is ACD.",
    [
        "The direct routing overview says you route voice, SMS, and email to dedicated personnel, and the customer does not wait for the next available agent. The interaction is still ACD, still goes through a queue, and wrap-up codes are available. Direct routing is not supported for non-ACD interactions. The people who receive it must be On queue, or Off queue and Available with the Routing > Conversation – Accept Off-Queue permission.",
        "If that person is unavailable, Genesys Cloud routes to a backup agent or queue. Backup queues and voicemail need an in-queue flow. A backup queue then uses its own routing method, and only On queue agents there receive it. A backup agent must be On queue, or Off queue and Available. Designating the direct number and the agent-level backup is done through APIs, as the overview states. The call path the article describes is: the number’s flow, a data action that finds the user, Transfer to ACD, then the in-queue flow if the agent does not answer.",
    ],
    cites("direct", "routing", "inqueue"),
    fig("The named person is alerted through a queue. A backup is a second hop.", [
        ("num", "Number", "phone", 12, 40),
        ("flow", "Flow", "architect", 38, 40),
        ("ag", "Direct agent", "agent", 64, 22),
        ("bk", "Backup", "queue", 64, 70),
    ], [("num", "flow"), ("flow", "ag"), ("ag", "bk")]),
    "Trace one direct call",
    [
        ("Customer", "Number", "Mapped flow", "Not a queue menu.", "Voice, SMS, or email"),
        ("Flow", "Data action", "User id", "Then Transfer to ACD.", "The queue still exists"),
        ("Agent", "Status", "On queue, or off queue and available", "The off-queue case needs the permission.", "Wrap-up is still ACD"),
        ("Miss", "In-queue flow", "Backup agent or queue", "The backup queue uses its own method.", "APIs designate the number"),
    ],
    [
        q("Direct routing media on the overview are:", "Voice, SMS, and email", ["Chat only", "Web messaging only", "Forecasts"], "The overview says those three."),
        q("A direct-routing interaction is:", "An ACD interaction through a queue, with wrap-up", ["A non-ACD call", "A bullseye ring", "A schedule"], "The overview says non-ACD interactions are not supported."),
        q("An agent who is Off queue can receive it when:", "Their status is Available and they have Routing > Conversation – Accept Off-Queue", ["They are logged out", "They fail the 7-day lookback", "They are only a forecast"], "On queue also qualifies, without that extra clause."),
        q("A backup queue routes with:", "The routing method configured on that backup queue, to On queue agents", ["The direct agent’s personal score", "Disregard skills always", "A long-term forecast"], "The overview separates backup agents from backup queues."),
        q("Designating the direct number, on this overview, is done:", "Through APIs", ["Only by renaming the queue", "By a bullseye ring", "By publishing a bot"], "Agent-level backup configuration is also listed as an API prerequisite."),
        q("Voicemail for a missed direct voice call depends on:", "An in-queue flow", ["A skill expression filter", "Option 1 bullseye groups", "The forecast editor"], "The overview says backup distribution to voicemail needs that flow."),
    ],
    [("Media", "Voice, SMS, email."), ("Still ACD", "Queue and wrap-up."), ("Status", "On queue, or off queue and available with the permission."), ("Backup", "In-queue flow, then agent or queue.")],
    "Write the miss path",
    ["The media.", "The agent status you will allow.", "Whether the backup is an agent or a queue.", "The in-queue flow’s job."],
    "The miss path names a backup and does not call the interaction non-ACD.",
    ("Personal line", "A premium caller’s DID is forwarded as a non-ACD call so wrap-up will not be required.", "The overview does not support direct routing for non-ACD interactions.", "The queue was removed to save a step.", "Put Transfer to ACD back, and decide the wrap-up mode on that queue."),
))

add(lesson(
    "k-scores", "Preferred scores are 0 to 100, and the list has a size", "Advanced", 13,
    "Architect’s agent-score collection supports 20 pairs unless Customer Care raises it. More than 20 fails a call flow.",
    [
        "The advanced routing overview says a preferred-agent score is the agent’s priority, from 0 to 100, and the highest score is the most preferred. Its example sets a case owner to 100 and backup agents to 90. If you do not have a preference, it says set the score to 100. In Architect, an agent-score collection supports up to 20 pairs. You can ask Customer Care to raise that maximum to 100. If a call flow supplies more than 20 pairs, the action takes the Failure path, and errorType is the string TooManyPreferredAgents. Email, chat, and message flows use their flow error handling instead.",
        "The same overview says that for email, messaging, and inbound callbacks, preferred agent routing means Genesys Cloud no longer tries the last agent who handled the interaction. Scheduled callbacks are unaffected. Preferred-agent rings on the settings article expand up to six rings, with the same 2-second to 72-hour timing note used elsewhere on that page. Bullseye still considers preferred agents whether or not they have the required skills.",
    ],
    cites("routing", "routing-settings", "bullseye"),
    fig("Higher score first. A list past 20 pairs fails the call flow.", [
        ("own", "Score 100", "agent", 22, 28),
        ("bak", "Score 90", "agent", 22, 70),
        ("list", "20 pairs", "architect", 58, 40),
        ("fail", "Failure", "phone", 86, 40),
    ], [("own", "list"), ("bak", "list"), ("list", "fail")]),
    "Set two scores and a limit",
    [
        ("Owner", "100", "Most preferred", "Backups at 90 in the example.", "0 to 100"),
        ("List", "MakeList", "Up to 20 pairs", "Ask Customer Care to raise the maximum to 100.", "Not a silent truncation"),
        ("Overflow", "Call flow", "Failure", "errorType TooManyPreferredAgents.", "Other flow types use their own error handling"),
        ("Last agent", "Email and messaging", "Not retried", "Inbound callbacks too.", "Scheduled callbacks stay as they are"),
    ],
    [
        q("A preferred-agent score runs from:", "0 to 100, and the highest is the most preferred", ["1 to 5, like a bullseye ring", "0 to 50 skills", "1 to 7 days"], "The advanced routing overview states that range."),
        q("The Architect collection supports, before a Customer Care increase:", "20 agent-score pairs", ["5 pairs", "6 pairs", "500 pairs"], "The increase maximum on that page is 100."),
        q("A call flow that supplies more than 20 pairs:", "Takes Failure, with errorType TooManyPreferredAgents", ["Drops the extras and alerts the rest", "Switches to bullseye", "Publishes the flow"], "Email, chat, and message flows use their flow error handling."),
        q("With preferred agent routing, email and messaging:", "Are no longer routed to the last agent who handled them", ["Always use last-agent routing", "Become non-ACD", "Skip the queue"], "Inbound callbacks are in that sentence. Scheduled callbacks are not."),
        q("If you have no preference among preferred agents, the overview says set the score to:", "100", ["0", "50", "7"], "The example uses 90 only for backups when you do have a preference."),
        q("Preferred agents inside bullseye are considered:", "Whether or not they have the required skills", ["Only after every skill is removed", "Only on the long-term forecast", "Only if the filter is valid"], "The bullseye overview says so."),
    ],
    [("0 to 100", "Highest is most preferred."), ("20", "The collection size, unless Customer Care raises it."), ("Too many", "Call-flow Failure."), ("Last agent", "Not used for email, messaging, or inbound callbacks under preferred routing.")],
    "Check a preferred list",
    ["The highest score.", "The number of pairs.", "What a 21st pair does in a call flow.", "Whether scheduled callbacks change."],
    "The list is within 20, or the failure path is drawn.",
    ("Twenty-first agent", "A call flow builds a preferred list of 25 account owners and the VIP calls fail in Architect.", "errorType would be TooManyPreferredAgents.", "The collection limit was treated as a display limit.", "Cut the list to 20 or ask Customer Care about the increase to 100, and handle Failure."),
))
