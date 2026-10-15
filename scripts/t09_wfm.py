from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "wfm",
    "title": "Workforce management",
    "kicker": "WEM",
    "accent": 2,
    "summary": "Business units, management units, service goals, schedules, adherence, and time off. WFM is a CX 3 capability.",
    "lessons": [],
}
def add(item):
    TRACK["lessons"].append(item)

add(lesson(
    "w-map", "WEM is a set of products, and WFM is one of them", "Core", 12,
    "Recording, screen recording, quality, performance, speech and text analytics, and workforce management are the WEM list.",
    [
        "The WEM article names those capabilities together. WFM is the planning half: business units, management units, service goal templates, planning groups, activity codes, schedules, adherence, intraday, and time off. Quality, recording, and speech analytics are the other half and have their own tracks in this lab.",
        "The overview places WEM on CX 3. A CX 1 org does not grow a forecast by publishing an Architect flow. The Workforce Management certification on the education catalog is the specialist exam for this half, with the WEM – Workforce Management course as the listed preparation.",
    ],
    cites("wem", "overview", "certs"),
    fig("WFM plans. QM and analytics listen. They are siblings.", [
        ("w", "WFM", "wem", 18, 40),
        ("q", "QM", "wem", 46, 22),
        ("s", "STA", "bot", 46, 68),
        ("cx", "CX 3", "region", 78, 40),
    ], [("cx", "w"), ("cx", "q"), ("cx", "s")]),
    "Separate the WEM siblings",
    [
        ("Scope", "Package", "CX 3", "WEM starts there.", "CX 4 includes it"),
        ("WFM", "Plan", "Schedules and adherence", "Business units and management units.", "Not an evaluation form"),
        ("QM", "Listen", "Forms and coaching", "A different admin.", "Next track"),
        ("Cert", "Catalog", "Workforce Management", "Its own specialist exam.", "Prep course is listed"),
    ],
    [
        q("WEM arrives with which package in the overview?", "CX 3", ["CX 1", "A trunk", "An RFC"], "Higher packages include it."),
        q("The WEM article’s list includes:", "Recording, screen recording, QM, performance, STA, and WFM", ["Only SIP", "Only bots", "Only OAuth"], "Those are the named capabilities."),
        q("Service goal templates belong to:", "Workforce management", ["Secure call flows", "DCVP", "AppFoundry"], "The WEM article lists them under WFM."),
        q("The specialist certification for this work is named:", "Workforce Management Certification", ["GC-GCD only", "A Cisco exam", "Architect only"], "The catalog lists it with the WEM – Workforce Management course."),
        q("An evaluation form is:", "Quality management, not the forecast", ["A business unit", "A number plan", "A ring"], "Keep the siblings apart."),
        q("CX 1 can be made to forecast by publishing a flow?", "No", ["Yes", "Only with a bot", "Only with 988"], "The package has to include WEM."),
    ],
    [("CX 3", "Where WEM starts."), ("WFM objects", "Business units, management units, goals, plans, schedules, adherence, time off."), ("Sibling", "QM and STA are not the schedule."), ("Cert", "Workforce Management, with the listed course.")],
    "Sort eight nouns",
    ["Mark each as WFM, QM, or telephony.", "Business unit, evaluation form, Edge, service goal, transcript, trunk, time off, screen recording.", "Name the package that first includes WEM."],
    "The telephony nouns are not in the WFM column.",
    ("Forecast on CX 1", "The project plan promises schedules. The org is CX 1.", "Overview: WEM is CX 3.", "The package does not contain the product.", "Change the license or cut the scope."),
))

add(lesson(
    "w-bu", "Business units and management units", "Core", 12,
    "A business unit is the planning container. A management unit is the group of agents you actually schedule.",
    [
        "The WEM article tells you to configure business units and management units before schedules. Agents in a management unit share the planning rules you are about to write. A queue is not a management unit. Queue membership decides who can receive an interaction. The management unit decides who is on the schedule.",
        "Splitting a management unit by every skill creates a puzzle the scheduler cannot solve. The bullseye article’s advice about proficiency groups exists so forecasting and routing describe the same people. If routing uses a skill the schedule has never heard of, the forecast will staff the wrong bodies.",
    ],
    cites("wem", "bullseye", "queues"),
    fig("Queue membership and the management unit are different groups.", [
        ("q", "Queue", "queue", 22, 40),
        ("mu", "Management unit", "wem", 58, 40),
        ("bu", "Business unit", "region", 84, 40),
    ], [("q", "mu"), ("mu", "bu")]),
    "Draw the containers",
    [
        ("Admin", "Business unit", "Create", "The planning container.", "One or more management units"),
        ("Admin", "Management unit", "Add agents", "The people you will schedule.", "Not automatically the queue roster"),
        ("Routing", "Skills", "Align", "Forecast the skills you route.", "Proficiency groups help"),
        ("Check", "Names", "Queue versus unit", "Write both.", "They may differ"),
    ],
    [
        q("A management unit is:", "The group of agents you schedule", ["A SIP trunk", "A division you cannot delete", "A bullseye ring"], "The WEM article lists it under WFM."),
        q("A queue and a management unit:", "Can contain different people", ["Must be identical", "Are the same object", "Are both phone trunks"], "One routes. One schedules."),
        q("The bullseye overview cares about WEM because:", "Skill expansion should stay compatible with forecasting", ["WEM configures TLS", "WEM buys DIDs", "WEM issues tokens"], "Proficiency groups are the compatible style."),
        q("Business unit sits:", "Above the management units as the planning container", ["Inside a single wrap-up code", "On the carrier", "In the OAuth client"], "The article names both objects."),
        q("Staffing a skill the schedule does not know about causes:", "A forecast that does not match who can actually take the call", ["A free region move", "An unpublished default only", "A 200 character error"], "Align routing and planning."),
        q("The 5,000 queue member cap is:", "A queue limit, not the definition of a management unit", ["The WFM cap", "The plan cap", "The token cap"], "Do not reuse the number as a WFM rule."),
    ],
    [("Business unit", "Planning container."), ("Management unit", "People you schedule."), ("Queue", "People who can be offered work."), ("Align skills", "Forecast what you route.")],
    "Name both groups",
    ["Business unit name.", "Management unit name.", "Queue name.", "One skill both sides share."],
    "The three names are not copies of each other unless you mean them to be.",
    ("Roster copied badly", "The schedule shows 40 agents. The queue has 12.", "Management unit imported from HR. Queue membership never updated.", "The containers were treated as one list.", "Decide which list is in charge of the schedule and which is in charge of routing, then reconcile."),
))

add(lesson(
    "w-goal", "Service goal templates are the planning target", "Core", 11,
    "The queue’s service level and the WFM template should describe the same promise.",
    [
        "The WEM article lists service goal templates among the objects you configure. The queue article is where the live percentage and target seconds are set, per media. If the template says 80 percent in 20 seconds and the queue says 80 percent in 60, you will staff for one promise and report another.",
        "This lab does not claim Genesys forecasts with Erlang C. Erlang models are classic telephony math. They are not stated in the WEM article. Use the template and the queue’s own target, and treat any external staffing formula as a side calculation you label as such.",
    ],
    cites("wem", "queues"),
    fig("One promise, two screens. They should match.", [
        ("q", "Queue target", "queue", 24, 40),
        ("t", "Template", "wem", 64, 40),
    ], [("q", "t")]),
    "Make the numbers agree",
    [
        ("WFM", "Template", "80/20 voice", "Write the planning target.", "Per media, like the queue"),
        ("Queue", "Voice panel", "Same pair", "Percentage and seconds.", "Email gets its own"),
        ("Lead", "Sign", "One promise", "Leadership should see one pair.", "Not a slide and a queue that differ"),
        ("Math", "External", "Label it", "If you use a classic formula, say it is not the product.", "The template is the product"),
    ],
    [
        q("Service goal templates are documented under:", "Workforce management in the WEM article", ["BYOC", "OAuth", "RFC 3261"], "That is their home."),
        q("The live voice target is configured on:", "The queue’s voice service level", ["The trunk", "The bot", "The token"], "Percentage and seconds, per media."),
        q("A template of 20 seconds and a queue target of 60 seconds means:", "You are planning and reporting different promises", ["They are averaged", "SIP fails", "The Edge fails over"], "Make them the same on purpose."),
        q("This lab treats Erlang-style formulas as:", "External math, not a documented Genesys forecast engine", ["The WFM algorithm", "A required queue field", "An RFC the product implements"], "The WEM article does not say Erlang."),
        q("Email and voice goals:", "Can differ, because each media has its own target", ["Must be identical", "Are illegal if different", "Are both 7 seconds"], "The queue article configures medias separately."),
        q("CX 1 includes these templates?", "No. WEM is CX 3.", ["Yes", "Only the template, not the schedule", "Only in FedRAMP"], "The overview places WEM on CX 3."),
    ],
    [("Template", "The planning promise."), ("Queue", "The reported promise."), ("Match them", "Or you staff the wrong target."), ("Erlang", "Not claimed as the Genesys engine.")],
    "Write one pair twice",
    ["Voice percentage and seconds.", "The same pair as the template.", "A different email pair.", "A note that any side formula is external."],
    "The two voice pairs match.",
    ("Slide versus queue", "The board deck says 20 seconds. The queue says 45.", "Template was never updated after the deck.", "Planners and the platform disagree.", "Pick one pair and type it in both places."),
))

add(lesson(
    "w-sched", "Schedules are the plan agents work", "Core", 11,
    "A schedule is built from the management unit, the goals, and activity codes. It is not a routing method.",
    [
        "The WEM article includes schedules and activity codes in the WFM list. Activity codes mark what an agent is supposed to be doing: on queue, break, meeting, training. On Queue, the routing status, is what ACD sees. An activity code that says “on queue” while the agent never selects On Queue is a schedule that routing cannot honor.",
        "Publishing a schedule does not add queue membership and does not change bullseye rings. If the schedule staffs a skill group that is not in the queue, the agents can be “working” and the queue can still starve.",
    ],
    cites("wem", "queues", "routing"),
    fig("The schedule says when. On Queue says the agent is actually available.", [
        ("s", "Schedule", "wem", 22, 40),
        ("a", "Activity", "agent", 52, 40),
        ("o", "On Queue", "queue", 82, 40),
    ], [("s", "a"), ("a", "o")]),
    "Connect the schedule to ACD",
    [
        ("Planner", "Activity codes", "Define", "On queue, break, meeting.", "Names people recognize"),
        ("Planner", "Schedule", "Generate", "From the management unit and the goal.", "Not from a routing method"),
        ("Agent", "Status", "On Queue", "During the on-queue activity.", "Otherwise ACD sees nobody"),
        ("Check", "Membership", "Still required", "The schedule does not join the queue.", "5,000 cap still applies"),
    ],
    [
        q("Activity codes are:", "WFM labels for what the agent should be doing", ["SIP methods", "OAuth grants", "Trunk subtypes"], "The WEM article lists them."),
        q("A schedule replaces On Queue?", "No. Routing still requires the status.", ["Yes", "Only for email", "Only for bots"], "The queue article’s status is separate."),
        q("A schedule adds queue members automatically?", "No", ["Yes", "Only under 30 minutes", "Only on CX 4"], "Membership is a queue setting."),
        q("Bullseye rings are changed by publishing a schedule?", "No", ["Yes", "Only ring 5", "Only the delay floor"], "Rings are routing configuration."),
        q("An on-queue activity with the agent left Available means:", "The schedule and ACD disagree", ["Perfect adherence", "A published flow", "A DCVP migration"], "Available is not On Queue."),
        q("The planning inputs named in this lesson are:", "Management unit, service goal, and activity codes", ["TLS ciphers", "Amazon root CAs", "Flow name length"], "Those are the WFM objects."),
    ],
    [("Activity", "What they should be doing."), ("On Queue", "What ACD requires."), ("Membership", "Still separate."), ("Schedule", "Does not edit rings.")],
    "Write one day",
    ["Three activity codes.", "When the agent must be On Queue.", "Which queue they must already belong to.", "What the schedule will not change."],
    "The day has a status, not only a color on a grid.",
    ("Green schedule, empty queue", "The forecast is met and the queue is unanswered.", "Agents in a meeting activity, or Available, during the on-queue block.", "The status never became On Queue.", "Coach the status, or fix the activity so the expectation is real."),
))

add(lesson(
    "w-intra", "Intraday and adherence compare the plan to the floor", "Core", 12,
    "Adherence is the gap between the activity you scheduled and the status the agent is actually in.",
    [
        "The WEM article lists real-time and historical adherence and intraday monitoring. Intraday is how you change today when the morning forecast was wrong. Adherence is how you see that agents are not in the activity you published. Neither one rewrites Architect.",
        "A queue that suddenly misses service level can be a routing bug or an adherence bug. Check On Queue counts before you add a bullseye ring. If the schedule said twelve and three are On Queue, the ring is not the first lever.",
    ],
    cites("wem", "queues"),
    fig("Intraday adjusts today. Adherence explains the gap.", [
        ("plan", "Plan", "wem", 18, 40),
        ("now", "Intraday", "agent", 48, 22),
        ("ad", "Adherence", "wem", 48, 70),
        ("q", "Queue", "queue", 80, 40),
    ], [("plan", "now"), ("plan", "ad"), ("now", "q")]),
    "Look at the floor before the ring",
    [
        ("Sup", "Intraday", "See the day", "The article’s monitoring view.", "Today, not next month"),
        ("Sup", "Adherence", "Compare", "Scheduled activity versus actual.", "Historical and real time"),
        ("Sup", "On Queue", "Count bodies", "Twelve planned, three present.", "That is the incident"),
        ("Sup", "Routing", "Later", "Change rings only if the bodies are actually there.", "Otherwise you widen onto nobody"),
    ],
    [
        q("Adherence compares:", "Scheduled activity and actual status", ["SIP and RTP", "CX 1 and CX 4", "Two trunks"], "The WEM article includes adherence for that reason."),
        q("Intraday monitoring is for:", "Adjusting the current day", ["Changing the AWS region", "Publishing a bot", "Buying DIDs"], "It is the same-day view."),
        q("A service-level miss with three of twelve agents On Queue is first:", "An adherence or staffing problem", ["A DCVP cipher problem", "A flow-name problem", "A 988 problem"], "Count the bodies before you edit rings."),
        q("Historical adherence is:", "Also in the WEM description, beside real-time", ["Removed", "A carrier feature", "An OAuth grant"], "The article says real-time and historical."),
        q("Adherence rewrites Architect flows?", "No", ["Yes", "Only common modules", "Only secure flows"], "It explains people, not tasks."),
        q("Widening bullseye when nobody is On Queue:", "Does not create agents", ["Fixes adherence", "Publishes the schedule", "Moves the region"], "The pool is still empty."),
    ],
    [("Intraday", "Today."), ("Adherence", "Plan versus actual."), ("Count On Queue", "Before you edit routing."), ("Historical", "Also documented.")],
    "Triage one red interval",
    ["Planned count.", "On Queue count.", "Whether you would touch a ring.", "What you would tell the supervisor."],
    "The ring is not the first edit.",
    ("Ring edited at noon", "Someone added a ring because service level dipped. The agents were in a meeting.", "Adherence: meeting. Routing change: extra ring.", "The lever was people.", "Revert the ring if it was only a reaction, and fix the activity or the meeting."),
))

add(lesson(
    "w-off", "Time off is a schedule change with a rule", "Core", 11,
    "Time-off requests are part of WFM. An approved request that nobody reflects on the schedule is a rumor.",
    [
        "The WEM article lists time-off requests beside schedules and adherence. A request that is approved in mail and never entered in WFM will show the agent as absent against a schedule that still expects them. Adherence will flag them, and the forecast will be wrong.",
        "Time off does not remove queue membership and does not set utilization. The agent who is off should not be On Queue. If they are, routing will still offer them work, and the schedule’s story will be fiction.",
    ],
    cites("wem", "queues"),
    fig("An approved request has to land on the schedule.", [
        ("req", "Request", "agent", 18, 40),
        ("ok", "Approved", "wem", 48, 40),
        ("sch", "Schedule", "wem", 78, 40),
    ], [("req", "ok"), ("ok", "sch")]),
    "Close the loop",
    [
        ("Agent", "Request", "In WFM", "The article lists the request.", "Not only in chat"),
        ("Sup", "Approve", "In the product", "Then the schedule can change.", "Mail is not the system"),
        ("Schedule", "Update", "The day", "Adherence should expect the absence.", "Otherwise it flags a good agent"),
        ("Agent", "Status", "Not On Queue", "Routing follows status.", "Time off is not a routing method"),
    ],
    [
        q("Time-off requests are documented as part of:", "Workforce management", ["BYOC", "Secure flows", "Number plans"], "The WEM article lists them."),
        q("An approval that never hits the schedule causes:", "Adherence to flag a planned absence as a miss", ["A trunk failure", "A token refund", "A region move"], "The plan and the floor disagree."),
        q("Time off removes queue membership?", "No", ["Yes", "Only over 5,000", "Only for email"], "Membership is separate. Status is what must change."),
        q("An agent on approved time off who stays On Queue will:", "Still be offered interactions", ["Be invisible to ACD", "Lose their division", "Drop SRTP"], "Routing watches status."),
        q("The system of record for the request should be:", "WFM, not a side conversation", ["A SIP header", "A participant data key", "A quiz"], "Otherwise the schedule cannot know."),
        q("CX package implication:", "WFM requests require the WEM package story, CX 3 and up", ["CX 1 includes scheduling", "No license is involved", "Only AppFoundry"], "The overview places WEM on CX 3."),
    ],
    [("Request", "In WFM."), ("Schedule", "Must show the absence."), ("Status", "Not On Queue."), ("Membership", "Unchanged.")],
    "Walk one request",
    ["Where it is entered.", "Who approves it.", "What the schedule should show.", "What the agent’s status should be."],
    "The four answers are in the product, not in chat.",
    ("Chat approval", "The agent is off. Adherence is red. The queue is short.", "Approval: a chat message. WFM request: none.", "The schedule never changed.", "Enter and approve the request in WFM so the day matches."),
))

add(lesson(
    "w-cert", "The workforce certification is a named exam", "Core", 10,
    "The catalog lists a Workforce Management specialist certification and a preparation course. It does not list a code this lab is willing to invent.",
    [
        "On the Genesys Education cloud exam page, Workforce Management Certification is a specialist exam. The recommended preparation is the course titled WEM – Workforce Management. Professional certification (GC-GCP) is a different exam, prepared by Implementation, Contact Center Administration, and Reporting and Analytics. You can sit more than one. They are not substitutes.",
        "Practice exams exist, 25 to 30 questions, without a voucher, from the announcement page. That practice exam is not this lab’s quiz. This lab’s quiz checks whether you can cite the product. The practice exam is Genesys’ own.",
    ],
    cites("certs", "cert-note", "wem"),
    fig("Specialist and professional exams are different catalog rows.", [
        ("p", "GC-GCP", "region", 22, 40),
        ("w", "WFM specialist", "wem", 62, 40),
    ], [("p", "w")]),
    "Pick the exam you mean",
    [
        ("Candidate", "Catalog", "Open the row", "Use the name on the page.", "Do not invent a code"),
        ("Candidate", "Prep", "WEM – Workforce Management", "The listed course.", "Not only this lab"),
        ("Candidate", "Practice", "Webassessor practice catalog", "No voucher, per the announcement.", "25 to 30 questions"),
        ("Candidate", "Work", "Still learn the product", "The exam does not configure your org.", "CX 3 still required to use WFM"),
    ],
    [
        q("The catalog name to study is:", "Workforce Management Certification", ["GCX-WFM as invented here", "CCNA Collaboration", "MS-721"], "This lab cites the catalog name and does not invent a specialist code."),
        q("The listed preparation course is:", "WEM – Workforce Management", ["Only the API course", "Only Architect", "A Cisco CVD"], "That is the catalog cell."),
        q("GC-GCP is:", "The professional certification, a different exam", ["The same exam", "A trunk subtype", "A ring count"], "The header code is GC-GCP."),
        q("The free practice exam described on the announcement is:", "25 to 30 questions, no voucher, in Webassessor", ["This lab’s quiz", "A live PSAP test", "An OAuth token"], "Use Genesys’ practice exam as well."),
        q("Passing the exam configures WFM in your org?", "No", ["Yes", "Only the business unit", "Only if you use implicit grant"], "Licenses and admin work remain."),
        q("Japanese availability, per the announcement, excludes:", "The Architect certification", ["All cloud exams", "WFM", "STA"], "The announcement says Architect is the exception."),
    ],
    [("Name", "Workforce Management Certification."), ("Prep", "WEM – Workforce Management."), ("Not GC-GCP", "Different exam."), ("Practice", "Genesys’ own, 25–30, no voucher.")],
    "Write your study list",
    ["Exam name from the catalog.", "Prep course name.", "Two product articles you will re-read.", "A note that this lab is not the practice exam."],
    "The list uses catalog names.",
    ("Wrong exam", "A candidate studies only GC-GCP and expects the WFM specialist badge.", "Catalog: two different rows.", "The professional exam’s prep courses are Implementation, Administration, and Reporting.", "Open the Workforce Management row and its own course."),
))
