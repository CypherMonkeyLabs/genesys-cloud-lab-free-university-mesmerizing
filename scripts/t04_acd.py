from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "acd",
    "title": "ACD routing",
    "kicker": "Routing",
    "accent": 1,
    "summary": "Standard, bullseye, preferred, predictive, and conditional routing, plus the two scoring methods.",
    "lessons": [],
}
def add(item):
    TRACK["lessons"].append(item)

add(lesson(
    "r-methods", "Five routing methods", "Core", 12,
    "Standard, predictive, bullseye, preferred agent, and conditional group routing are the methods on a queue.",
    [
        "The routing settings article lists those five. Standard is the default. It offers the interaction to the next agent according to the evaluation method you picked. Bullseye adds rings that widen the pool. Preferred agent tries a named pool first. Predictive uses historical outcomes against a KPI you select. Conditional group routing shares a group of agents across queues when a KPI rule says the other queue can spare them.",
        "Methods can time out into another method. Preferred agent’s timeout can fall back to standard, bullseye, or conditional group routing. Predictive’s timeout falls back to standard. If you only memorize the names, you will mis-set the fallback and the queue will look “stuck” when it is doing the second method.",
    ],
    cites("routing", "routing-settings"),
    fig("One queue, one method, and a documented fallback.", [
        ("q", "Queue", "queue", 18, 40),
        ("m", "Method", "architect", 48, 22),
        ("fb", "Fallback", "agent", 78, 60),
    ], [("q", "m"), ("m", "fb")]),
    "Pick a method and its timeout",
    [
        ("Admin", "Queue", "Open routing", "The method is a queue setting.", "Standard is the default"),
        ("Admin", "Method", "Choose", "Five documented choices.", "Do not invent a sixth"),
        ("Admin", "Timeout", "Set", "Preferred and predictive both expire.", "Name the fallback"),
        ("ACD", "Agents", "Offer", "Only eligible agents are offered.", "On Queue and utilization still apply"),
    ],
    [
        q("The default routing method is:", "Standard", ["Predictive", "Bullseye", "Preferred"], "The settings article says standard is the default."),
        q("Predictive routing’s documented timeout fallback is:", "Standard routing", ["Disconnect", "A new org", "Voicemail only"], "The settings article describes standard as that fallback."),
        q("Conditional group routing exists to:", "Share agent groups across queues without breaking the other queue’s KPI", ["Replace SIP", "Encrypt RTP", "Publish Architect"], "The overview describes KPI-and-availability rules."),
        q("How many routing methods does the settings article list?", "Five", ["Three", "Two", "Eleven"], "Standard, predictive, bullseye, preferred, conditional group."),
        q("Preferred agent timeout may fall back to:", "Standard, bullseye, or conditional group", ["Only disconnect", "Only a bot", "Only FedRAMP"], "The settings article lists those options."),
        q("Changing the method without reading the fallback causes:", "A queue that looks stuck while it is in the second method", ["A region move", "A license refund", "An unpublished name"], "The timeout is part of the design."),
    ],
    [("Five", "Standard, predictive, bullseye, preferred, conditional."), ("Default", "Standard."), ("Predictive fallback", "Standard."), ("Preferred fallback", "Standard, bullseye, or conditional.")],
    "Name the method for three queues",
    ["A simple longest-idle skills queue.", "A queue that should widen skills over time.", "A queue that should try last month’s best closer first, with a KPI.", "Write the fallback for the third."],
    "Each queue has a method and a fallback.",
    ("Stuck VIP", "VIP callers wait the full timeout even though general agents are idle.", "Method: preferred. Fallback: none was set, so the timeout sits.", "Preferred only searches the preferred pool until it expires.", "Set the timeout and a standard or bullseye fallback, then test with a non-preferred idle agent."),
))

add(lesson(
    "r-eval", "All skills, best available, or disregard", "Core", 13,
    "The evaluation method is how standard and bullseye decide that an agent “has the skills.”",
    [
        "All skills matching selects the longest-idle agent who has every required skill. Proficiency is not the sort. Best available skills looks at the 100 longest-idle agents who have the required skills and then picks the highest average proficiency, with idle time as the tie-break. Disregard skills, next agent, offers the interaction to the first available agent and ignores skills.",
        "The evaluation article also says routing considers agent activity from the previous 7 days and skips inactive agents. A skill you added this morning on an agent who has not been active does not behave like a skill on someone who has been taking calls all week. Bullseye’s strict rings want all-skills or best-available. Disregard skills makes the rings much less meaningful.",
    ],
    cites("evaluation", "bullseye"),
    fig("All-skills sorts by idle time. Best-available sorts by proficiency inside the idle window.", [
        ("all", "All skills", "agent", 22, 36),
        ("best", "Best of 100", "agent", 55, 36),
        ("none", "Disregard", "queue", 84, 36),
    ], [("all", "best"), ("best", "none")]),
    "Two agents, one method",
    [
        ("Interaction", "ACD", "Needs Billing and Spanish", "Both skills are required.", "Evaluation decides the rest"),
        ("All skills", "Leo", "Longest idle with both", "Amina lacks Spanish and is out.", "Proficiency is not the sort"),
        ("Best", "Window", "100 longest idle", "Then highest average proficiency.", "Idle breaks the tie"),
        ("Disregard", "Anyone", "First free agent", "Skills are ignored.", "Rings stop meaning much"),
        ("Profile", "7 days", "Activity", "Inactive agents are not in the pool.", "A brand-new skill is not magic"),
    ],
    [
        q("All skills matching breaks ties by:", "Longest idle among agents who have every skill", ["Highest proficiency", "Lowest license cost", "Alphabetically"], "The evaluation article describes longest-idle, not proficiency, for this method."),
        q("Best available skills first narrows to:", "The 100 longest-idle agents who have the required skills", ["Every agent in the org", "Only preferred agents", "Only CX 4 users"], "Then it compares average proficiency."),
        q("The tie-break inside best available skills is:", "Idle time", ["Division name", "SIP response code", "Flow name length"], "Proficiency first, idle time second."),
        q("Disregard skills means:", "The next available agent, skills ignored", ["All skills are removed from the org", "Bullseye adds a sixth ring", "Predictive is disabled globally"], "It is an evaluation method, not a data wipe."),
        q("Activity considered for routing is from:", "The previous 7 days", ["The previous 7 minutes", "The previous 30 days only", "All time"], "The evaluation article states 7 days."),
        q("Bullseye skill removal is most meaningful with:", "All skills matching or best available skills", ["Disregard skills", "No evaluation at all", "A secure flow"], "The bullseye article says those strict methods are where removal matters."),
    ],
    [("All", "Longest idle with every skill."), ("Best", "Top 100 longest idle, then proficiency."), ("Disregard", "Skills do not filter."), ("7 days", "Inactive agents drop out.")],
    "Score three agents on paper",
    ["Give two agents both skills and different idle times.", "Give a third agent higher proficiency and less idle time.", "Say who wins under all-skills.", "Say who wins under best-available."],
    "You can predict the winner before you click the simulator.",
    ("Proficiency surprise", "The five-star agent never gets the call. A one-star agent does.", "Evaluation: all skills matching. Five-star agent idle: 10 seconds. One-star agent idle: 20 minutes. Both have the skills.", "All-skills ignores proficiency.", "Switch to best available skills if proficiency is the policy, or accept longest-idle as the policy."),
))

add(lesson(
    "r-score", "Conversation score and priority score", "Core", 12,
    "One priority point on conversation score is worth 60,000 milliseconds of arrival time.",
    [
        "Conversation score combines arrival time and priority. The evaluation article says one priority point equals 60,000 milliseconds, so a higher priority jumps the line as if it had arrived earlier. Priority score uses the priority value first and time-in-queue only as a tie-break. When queues that the same agent serves use different scoring methods, Genesys Cloud gives precedence to queues using priority score.",
        "A priority 5 interaction that arrived now outranks a priority 0 interaction that arrived four minutes ago, because five points are 300,000 milliseconds, which is five minutes. That arithmetic is the article’s rule, and it is the rule the routing simulator uses. It is not a reason to set every queue to priority 10. If everything is urgent, nothing is.",
    ],
    cites("evaluation"),
    fig("Priority pulls an interaction forward in time under conversation score.", [
        ("old", "Priority 0", "phone", 22, 60),
        ("new", "Priority 5", "phone", 58, 28),
        ("ag", "Agent", "agent", 84, 44),
    ], [("new", "ag")]),
    "Who is offered when one agent becomes free",
    [
        ("Call A", "Queue", "Priority 0, waited 4 min", "Conversation rank is its arrival.", "No boost"),
        ("Call B", "Queue", "Priority 5, just arrived", "Five points equal five minutes.", "It ranks ahead of A"),
        ("Agent", "ACD", "One slot", "Only one interaction is chosen.", "The other keeps waiting"),
        ("Other queue", "Priority score", "Different method", "Priority-score queues win across methods.", "Do not mix them by accident"),
    ],
    [
        q("One conversation-score priority point equals:", "60,000 milliseconds", ["1 millisecond", "1 hour", "7 days"], "The evaluation article states 60,000 ms."),
        q("A priority 5 call that just arrived versus a priority 0 call that arrived 4 minutes ago:", "The priority 5 call ranks first under conversation score", ["The older call always wins", "Neither is offered", "The trunk resets"], "Five minutes of equivalent wait beats four minutes."),
        q("Priority score orders by:", "Priority value, then time in queue", ["Idle agent name", "Flow Insights", "License cost"], "Time is the tie-break, not the main key."),
        q("If one queue uses priority score and another uses conversation score, an agent shared by both sees:", "Priority-score queues take precedence", ["A random queue", "Only email", "Only bullseye"], "The evaluation article describes that cross-queue rule."),
        q("Setting every interaction to priority 10:", "Removes the meaning of priority", ["Is required for predictive", "Publishes the in-queue flow", "Lowers the concurrent peak"], "Relative priority is the point of the score."),
        q("The simulator’s conversation rank subtracts priority times 60,000 from arrival so that:", "Higher priority sorts as if it arrived earlier", ["Higher priority waits longer", "Skills are removed", "The Edge fails over"], "That is the same relationship the article describes."),
    ],
    [("60,000 ms", "One conversation-score point."), ("Priority score", "Value first, time second."), ("Cross queue", "Priority-score queues take precedence."), ("Do not inflate", "If all priorities match, you bought nothing.")],
    "Do the arithmetic",
    ["Compute 5 times 60,000 ms.", "Compare it with a 4 minute wait.", "Say which call wins.", "Say what changes if the queue uses priority score instead."],
    "You can explain the winner without opening the admin UI.",
    ("Callback jumped the board", "A fresh callback is offered before a caller who has waited six minutes.", "Callback priority: 10. Conversation score is on. 10 points equal 10 minutes.", "The score is working. The priority value is the policy.", "Lower the callback priority or switch the scoring method if the board should be first-in."),
))

add(lesson(
    "r-bullseye", "Bullseye rings widen the target", "Core", 14,
    "Up to five rings. A delay from 2 seconds to 72 hours. Up to 50 skills removed on a ring.",
    [
        "Bullseye starts with the tightest pool and expands. The settings article first says to define up to five rings. Later on that same page, the skill-removal steps and the preferred-agent steps say up to six rings, and the advanced routing overview says create up to six rings. The delay between rings is from 2 seconds through 259,200 seconds, which is 72 hours. A ring can remove up to 50 skills. Two expansion styles are documented: add groups that share the skill at a lower proficiency, which stays compatible with WEM forecasting, or remove skills on outer rings.",
        "Inner-ring agents stay preferred over outer-ring agents even after the ring opens. Preferred agents are considered even when they lack the required skills. Agents who are busy, fully utilized, or logged out are not available. The routing simulator in this lab removes a skill on ring 2 after the ring 1 delay, which is the skill-removal style, not a second product.",
    ],
    cites("bullseye", "routing-settings", "preferred"),
    fig("Ring 1 is tight. Ring 2 drops a skill after the delay.", [
        ("r1", "Ring 1", "agent", 30, 36),
        ("r2", "Ring 2", "agent", 58, 36),
        ("call", "Call", "phone", 12, 70),
    ], [("call", "r1"), ("r1", "r2")]),
    "Spanish falls off after 8 seconds",
    [
        ("Call", "Ring 1", "Billing and Spanish", "Only bilingual agents.", "Delay 8 seconds"),
        ("ACD", "Agents", "None free", "The ring does not skip early just because you are impatient.", "Wait the delay"),
        ("Call", "Ring 2", "Drop Spanish", "Billing remains.", "Up to 50 removals"),
        ("ACD", "Amina", "Billing only", "She becomes eligible on ring 2.", "Unless a preferred agent already matched"),
        ("WEM", "Design", "Proficiency groups", "Same skills, lower proficiency, if forecasting must stay aligned.", "The other expansion style"),
    ],
    [
        q("The settings article first tells you to define up to:", "Five rings", ["Three rings", "Ten rings", "Fifty rings"], "That opening instruction says five. A later step on the same page, and the advanced routing overview, say six. Confirm the control in the queue."),
        q("The shortest documented delay between rings is:", "2 seconds", ["0 seconds", "7 seconds", "30 minutes"], "2 seconds is the floor. 7 seconds is the voice alerting floor, a different timer."),
        q("The longest documented ring delay is:", "259,200 seconds, 72 hours", ["59 seconds", "24 hours", "7 days"], "The queue article states 259,200 seconds."),
        q("Skills you may remove on one ring:", "Up to 50", ["Up to 5", "Unlimited", "None"], "The settings and queue articles state 50."),
        q("Which expansion style stays aligned with WEM forecasting?", "Groups that share the skill at a lower proficiency", ["Deleting the queue", "Disregard skills", "Removing the division"], "The bullseye overview recommends that style for WEM compatibility."),
        q("After an outer ring opens, an inner-ring agent who becomes free:", "Still outranks the outer ring", ["Is ignored", "Is logged out", "Loses their skills"], "The overview says inner rings keep priority."),
    ],
    [("Ring count", "First instruction: five. Later steps and the overview: six. Confirm in the queue."), ("2 seconds to 72 hours", "The delay range."), ("50 skills", "The removal cap."), ("Two styles", "Lower proficiency groups, or remove skills.")],
    "Configure two rings on paper",
    ["Write ring 1’s skills and delay.", "Write the skill ring 2 removes.", "Say who wins if a ring 1 agent frees up late.", "Say which style you would use if WFM forecasts this queue."],
    "The rings match a policy someone can test in the simulator.",
    ("Instant widen", "Every call hits general agents immediately. The bilingual team never sees them.", "Ring 1 delay: 2 seconds. Bilingual agents are usually on another call for longer than that.", "The ring is legal and too short for the real handle pattern.", "Lengthen the delay so ring 1 has a chance, and watch abandon before you lengthen it again."),
    "The settings article’s first bullseye instruction says five rings. A later step on that page says up to six, and the advanced routing overview says create up to six. Count the rings the queue offers before you design a sixth.",
))

add(lesson(
    "r-preferred", "Preferred agents are tried first", "Core", 13,
    "A preferred agent is considered even without the required skills, and only if they are a member of the queue and On Queue.",
    [
        "The behavior article describes a score and a timeout. In its example the first window tries the highest-score preferred agent, and the next window opens the rest of the preferred pool. Selection among agents who meet the current score is by time since the last interaction. Full utilization removes an agent from consideration. Partial utilization does not. If no preferred agent is actually a member of the queue, the timeouts are skipped and routing moves on.",
        "Last-agent routing does not apply to email flows, only to direct queue routing in the cases the article allows. During transfers, preferred agents are excluded. A higher-priority interaction still jumps ahead of a preferred match for a lower-priority one. The simulator’s “preferred first” switch is this idea: if any preferred agent is eligible, the pool is only those agents.",
    ],
    cites("preferred", "bullseye"),
    fig("Preferred agents form the first pool, skills or not.", [
        ("call", "Call", "phone", 14, 40),
        ("pref", "Preferred", "agent", 48, 22),
        ("rest", "Everyone else", "agent", 48, 70),
    ], [("call", "pref")]),
    "Try Amina before the bilingual team",
    [
        ("Profile", "Queue", "Mark preferred", "She must already be a member.", "A non-member skips the timer"),
        ("Amina", "Status", "On Queue", "Off queue does not count.", "Full utilization does not count"),
        ("ACD", "Amina", "Offer", "She can lack Spanish and still be tried.", "Bullseye does not block her"),
        ("Timer", "Fallback", "Expire", "Then the configured fallback runs.", "Standard, bullseye, or conditional"),
        ("Transfer", "Rule", "Skip preferred", "Transfers do not use the preferred pool.", "The article says so"),
    ],
    [
        q("A preferred agent who is not a member of the queue:", "Causes the preferred timeouts to be skipped", ["Is added automatically", "Becomes the division owner", "Breaks SIP"], "The behavior article says the timeouts are skipped."),
        q("Preferred agents and required skills:", "They are considered even when the skills are missing", ["They must have every skill", "Skills are deleted", "Only on email"], "The bullseye and preferred articles both say this."),
        q("Full utilization does what to a preferred agent?", "Removes them from consideration", ["Raises their score to 100", "Publishes the flow", "Extends the 72 hour timer"], "Partial utilization still leaves them eligible."),
        q("Last-agent routing and email:", "Last-agent routing does not function for email flows", ["It is the only email method", "It requires CX 1", "It uses RTP"], "The behavior article excludes email flows."),
        q("Among preferred agents who meet the current score, the article selects by:", "Time since last interaction", ["Alphabetical name", "License cost", "Division"], "Idle time inside the score band."),
        q("A transfer to the queue:", "Does not use preferred agents", ["Always uses them", "Deletes them", "Requires a secure flow"], "The article excludes preferred agents during transfers."),
    ],
    [("Member + On Queue", "Both are required."), ("Skills", "Not required for a preferred agent."), ("Utilization", "Full means skip."), ("Email", "Last-agent routing does not apply.")],
    "Trace one preferred offer",
    ["Confirm membership.", "Confirm On Queue.", "Confirm they are not fully utilized.", "Name the fallback when the timer ends."],
    "You can say why the preferred agent was skipped.",
    ("Preferred ghost", "The VIP timer never seems to run. Calls hit the general pool immediately.", "Preferred user: not a member of this queue. Timeout configured: 120 seconds.", "Non-members cause the timeout to be skipped.", "Add them to the queue, then retest."),
))

add(lesson(
    "r-predict", "Predictive routing is a KPI model with a timeout", "Advanced", 14,
    "Predictive routing can run for everyone, in a comparison test, or at a fixed 80/20 split you cannot edit.",
    [
        "The queue article describes three modes. Comparison test mode measures predictive routing against a baseline. Use for all interactions sends everything through the model. Ongoing value monitoring keeps an 80 percent predictive and 20 percent baseline split, and the article says you cannot change that ratio. Genesys recommends leaving monitoring in place for months. The timeout still falls back to standard routing. If the queue has no interactions for 30 continuous days, predictive routing turns itself off and standard routing returns.",
        "The model needs history. A queue you created this morning does not have a KPI story yet. Comparison mode is how you earn the right to turn it on for everyone. The AI certification catalog treats predictive routing and predictive engagement as a study path of their own. Turning the feature on is not the same as passing that exam, and it is not the same as bullseye.",
    ],
    cites("queues", "routing", "certs"),
    fig("Eighty percent through the model, twenty percent through the baseline.", [
        ("in", "Interactions", "phone", 14, 40),
        ("p", "80 predictive", "bot", 48, 22),
        ("b", "20 baseline", "queue", 48, 68),
        ("std", "Standard timeout", "agent", 82, 40),
    ], [("in", "p"), ("in", "b"), ("p", "std")]),
    "Turn it on without lying to yourself",
    [
        ("Admin", "Mode", "Comparison", "Prove the KPI before you trust it.", "Do not start on all traffic"),
        ("Admin", "Monitor", "80/20", "The split is fixed.", "Leave it for months"),
        ("Model", "Timeout", "Standard", "A slow decision still has a fallback.", "The caller is waiting"),
        ("Queue", "Idle 30 days", "Auto off", "No traffic disables the model.", "Standard returns"),
        ("People", "Training", "Different skill", "The GPE and GPR certification is a course path.", "Not a queue toggle"),
    ],
    [
        q("Ongoing value monitoring splits traffic:", "80 percent predictive, 20 percent baseline, and you cannot change it", ["50/50", "100 percent", "A custom ratio"], "The queue article says the ratio is fixed."),
        q("Predictive routing turns itself off when:", "The queue has no interactions for 30 continuous days", ["An agent goes On Queue", "A ring delay hits 2 seconds", "You publish a flow"], "Standard routing is restored."),
        q("The timeout fallback is:", "Standard routing", ["Disconnect", "Bullseye only", "A secure flow"], "The queue and routing articles describe that fallback."),
        q("Comparison test mode is for:", "Measuring the model against a baseline before you trust it", ["Deleting skills", "Emergency calling", "OAuth"], "It is one of the three documented modes."),
        q("A brand-new queue is a weak predictive candidate because:", "The model learns from historical outcomes", ["New queues cannot use ACD", "Names are limited to 7 characters", "Satellites block it"], "The overview describes learning from historical contact-center data."),
        q("The AI – GPE & GPR certification is:", "A Genesys Education exam path, separate from clicking the queue setting", ["Required to create a queue", "An RFC", "The same exam as GC-GCD"], "The catalog lists it as its own certification."),
    ],
    [("Three modes", "Comparison, all interactions, 80/20 monitoring."), ("80/20", "Fixed."), ("30 days", "No traffic disables it."), ("Fallback", "Standard.")],
    "Choose a mode",
    ["Say why you would not start on all interactions.", "Write the 80/20 rule.", "Write the 30-day rule.", "Name the fallback."],
    "You can explain the mode without promising a KPI you have not measured.",
    ("Model went quiet", "A seasonal queue stopped using predictive routing in October.", "Last interaction: 32 days ago. Routing method now: standard.", "Thirty quiet days disable it.", "Turn it back on when the season starts, in comparison mode, and confirm new history is flowing."),
))

add(lesson(
    "r-conditional", "Conditional group routing borrows agents carefully", "Advanced", 12,
    "A rule is a KPI plus agent availability. The other queue must be able to spare the people.",
    [
        "The overview describes conditional group routing as sharing groups of agents between queues based on rules. A rule combines a KPI with availability so you do not pull agents off a queue that is already missing its service level. The settings article says you can build up to five rules. It is a routing method, not a bullseye ring and not a WFM schedule change.",
        "Use it when two queues are real neighbors, such as billing and billing overflow, and you can name the KPI that protects the donor queue. Do not use it as a silent way to empty a specialist queue. The agents still have to be On Queue, under utilization, and allowed by whatever evaluation method the target queue is using.",
    ],
    cites("routing", "routing-settings", "util"),
    fig("Overflow borrows agents only while the donor queue is healthy.", [
        ("src", "Donor queue", "queue", 18, 40),
        ("rule", "KPI rule", "architect", 48, 40),
        ("dst", "Overflow", "queue", 78, 40),
    ], [("src", "rule"), ("rule", "dst")]),
    "Borrow billing agents for overflow",
    [
        ("Admin", "Rule", "Service level", "Name the KPI that must hold.", "Up to five rules"),
        ("Admin", "Availability", "Spare agents", "The donor must actually have people free.", "On Queue still matters"),
        ("ACD", "Donor", "Check", "If the donor is failing its KPI, do not pull.", "That is the point of the rule"),
        ("Agent", "Utilization", "Capacity", "A full agent is not spare.", "Voice default is one call"),
    ],
    [
        q("A conditional routing rule combines:", "A KPI and agent availability", ["A SIP port and a codec", "A token and a region", "A prompt and a WAV"], "The overview defines a rule that way."),
        q("The settings article allows up to how many conditional rules?", "Five", ["One", "Fifty", "Two hundred"], "Five is the documented cap."),
        q("Conditional routing is a substitute for WFM scheduling?", "No. It is a routing method.", ["Yes", "Only on CX 1", "Only for email"], "Schedules live in WEM. This is ACD."),
        q("A donor queue missing its service level should:", "Not give up its agents", ["Be deleted", "Lose its division", "Start a secure flow"], "The rule exists to protect that KPI."),
        q("Agents pulled across still must be:", "On Queue and under their utilization cap", ["Off queue", "Fully utilized", "In a satellite region"], "Those filters are not removed by the rule."),
        q("Bullseye and conditional routing differ because:", "Bullseye widens skills on one queue. Conditional shares people across queues.", ["They are the same setting", "Both are OAuth grants", "Both are number plans"], "The overview describes both, separately."),
    ],
    [("Rule", "KPI plus availability."), ("Five", "Maximum rules."), ("Protect the donor", "Do not steal a failing queue’s agents."), ("Still ACD", "On Queue and utilization remain.")],
    "Write one rule",
    ["Name the donor queue.", "Name the KPI.", "Name the overflow queue.", "Say what should happen when the donor is already failing."],
    "The rule protects the donor in a sentence.",
    ("Raided specialists", "Spanish queue service level collapses every afternoon. Overflow looks fine.", "Conditional rule: no KPI, availability only.", "The donor was not protected.", "Add a service-level condition so the borrow stops while Spanish is already missing its target."),
))

add(lesson(
    "r-util", "Utilization and Not Responding", "Core", 13,
    "A fully utilized agent is skipped. An agent who ignores an alert becomes Not Responding.",
    [
        "Defaults from the utilization article: one voice call, one email, one callback, up to four chats, up to four messages, and up to four workitems. You can change the org default and a single agent. You can also decide which medias may interrupt which others. By default, calls and callbacks do not interrupt each other. Non-ACD calls are excluded unless you enable “Count non-ACD calls in utilization capacity” and set voice capacity to 1, which stops ACD alerts during personal calls.",
        "Voice alerting is 7 to 59 seconds. When it expires, the agent’s status becomes Not Responding and the interaction returns to the queue. Auto answer removes the alerting timeout, though the agent still gets an audio alert. Preview calls count as callbacks. The preferred-agent article uses the same utilization idea: a full agent is not offered the interaction.",
    ],
    cites("util", "queues", "preferred"),
    fig("Capacity gates the offer. Alerting gates the answer.", [
        ("acd", "ACD", "queue", 16, 40),
        ("cap", "Utilization", "agent", 46, 22),
        ("alert", "Alert", "phone", 46, 70),
        ("nr", "Not Responding", "agent", 80, 70),
    ], [("acd", "cap"), ("cap", "alert"), ("alert", "nr")]),
    "One voice call, then the alert",
    [
        ("Agent", "Voice", "Already on a call", "Default capacity is one.", "The next call skips them"),
        ("Admin", "Interrupt", "Email versus voice", "You choose what may interrupt.", "Calls and callbacks do not interrupt each other by default"),
        ("ACD", "Agent", "Alert 8 seconds", "Inside the 7 to 59 window.", "A legal timeout"),
        ("Agent", "Miss", "Not Responding", "The call returns to the queue.", "Auto answer would skip this timer"),
        ("Personal", "Toggle", "Count non-ACD", "Optional. Stops ACD alerts during personal calls.", "Voice capacity must be 1"),
    ],
    [
        q("Default simultaneous voice calls are:", "1", ["4", "8", "0"], "The utilization article says one voice call."),
        q("Default chats are up to:", "4", ["1", "2", "10"], "Chats, messages, and workitems default to four."),
        q("Voice alerting must be between:", "7 and 59 seconds", ["2 seconds and 72 hours", "30 minutes and a day", "Exactly 4 seconds"], "That range is on the queue article."),
        q("When alerting expires, status becomes:", "Not Responding, and the interaction returns to the queue", ["On Queue", "Preferred", "CX 4"], "The queue article describes that transition."),
        q("Auto answer and the alerting timeout:", "The timeout does not apply, but an audio alert still plays", ["Auto answer is forbidden", "Auto answer sets Not Responding immediately", "Auto answer deletes the queue"], "The queue article says the option is hidden and an audio alert remains."),
        q("Calls and callbacks interrupting each other is:", "Prevented by default", ["Required", "Only for email", "A bullseye ring"], "The utilization article says the default avoids that interrupt."),
    ],
    [("Defaults", "1 call, 1 email, 1 callback, 4 chats, 4 messages, 4 workitems."), ("Alert", "7–59 seconds, then Not Responding."), ("Auto answer", "No alerting timeout. Audio alert remains."), ("Non-ACD", "Excluded unless you opt in.")],
    "Set one agent’s capacity",
    ["Leave voice at 1 and say why.", "Set chats to 2 and say what you changed from the default.", "Pick an alerting timeout inside 7 to 59.", "Say what Not Responding means for the caller."],
    "The numbers are inside the documented ranges.",
    ("Double voice", "Agents complain they receive a second call while they are talking.", "Agent utilization voice capacity: 2. Org default: 1.", "The agent override allows a second call.", "Set that agent back to 1 unless the program truly wants two voice conversations."),
))
