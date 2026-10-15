from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "queues",
    "title": "Queues, skills, and wrap-up",
    "kicker": "ACD objects",
    "accent": 4,
    "summary": "Queue media settings, skills, wrap-up codes, callbacks, and service level.",
    "lessons": [],
}
def add(item):
    TRACK["lessons"].append(item)

add(lesson(
    "q-create", "Create the queue in a division", "Core", 11,
    "The queue is a named waiting line in one division, with at most 5,000 members.",
    [
        "Menu path in the article is User Management, then Queues. You set a unique name without special characters, an optional peer id for an external platform, the division, and an optional default language. You can copy settings and members from an existing queue and edit after.",
        "Copying a queue copies its routing method too. If the source uses predictive routing or a five-ring bullseye, the copy is not a blank standard queue. Read the routing tab after the copy. The new queue still needs its own in-queue flow assignment if you do not want the org default.",
    ],
    cites("queues", "divisions"),
    fig("A queue is created inside one division.", [
        ("div", "Division", "region", 22, 40),
        ("q", "Queue", "queue", 55, 40),
        ("m", "Members", "agent", 82, 40),
    ], [("div", "q"), ("q", "m")]),
    "Create Billing voice",
    [
        ("Admin", "Queues", "Create", "Open User Management, Queues.", "Name it without special characters"),
        ("Admin", "Division", "Home or EMEA", "One division.", "Move later if you guessed wrong"),
        ("Admin", "Copy", "Optional", "Copy members only if you mean to.", "Check the routing tab after"),
        ("Admin", "Save", "General tab", "The article says the configuration opens on General.", "Then set media"),
    ],
    [
        q("Queue names must be:", "Unique and free of special characters", ["Unique across every Genesys customer", "Exactly the division name", "A SIP URI"], "The article states both rules."),
        q("Member cap is:", "5000", ["200", "50", "5"], "5,000 members per queue."),
        q("The division on the queue controls:", "Which role grants can administer it", ["The RTP codec", "The login region", "The token price"], "Divisions are the access boundary."),
        q("Copy settings and members:", "Is optional and still needs a review of routing", ["Is required", "Deletes the source", "Publishes Architect"], "The copy includes configuration, which includes routing."),
        q("Peer id on a queue is for:", "External platform synchronization", ["Emergency calling", "OAuth", "Bullseye ring 1"], "The article describes the peer id that way."),
        q("Default language on the queue is:", "Optional", ["Always en-US", "Forbidden", "A trunk setting"], "The article calls it non-mandatory."),
    ],
    [("Name", "Unique, no special characters."), ("5,000", "Member cap."), ("Division", "Chosen at create."), ("Copy", "Review routing after.")],
    "Create a paper queue",
    ["Write a legal name.", "Name the division.", "Say whether you will copy.", "Say what you will check if you do."],
    "The queue can be created without a naming or division surprise.",
    ("Illegal name", "The save fails.", "Name: Billing/voice.", "The slash is a special character.", "Use Billing voice."),
))

add(lesson(
    "q-skills", "Skills and proficiency are on the agent", "Core", 12,
    "The queue asks for skills. The agent profile holds them. Evaluation decides whether proficiency matters.",
    [
        "ACD skills are tags with a proficiency. All-skills matching ignores the number and demands the tag. Best available skills uses the average proficiency inside the 100 longest-idle window. A skill the interaction does not require does not help or hurt that interaction.",
        "Bullseye can express the same skill at a lower proficiency on an outer ring by using groups, which the overview prefers when WEM forecasts must stay stable. Removing the skill entirely is the other style. Agents inactive for the 7 day window described in the evaluation article are not candidates even if their profile looks perfect.",
    ],
    cites("evaluation", "bullseye", "routing"),
    fig("The interaction asks. The profile answers.", [
        ("need", "Billing 3", "queue", 20, 40),
        ("a", "Amina 5", "agent", 55, 22),
        ("b", "Leo 1", "agent", 55, 68),
    ], [("need", "a"), ("need", "b")]),
    "Staff a bilingual ring",
    [
        ("Admin", "Skill", "Create Billing", "The tag exists before the queue can require it.", "Proficiency lives on the user"),
        ("Admin", "Users", "Assign", "Give the specialist pool a high proficiency.", "Give overflow a lower one"),
        ("Queue", "Evaluation", "Best", "Proficiency now matters.", "All-skills would ignore it"),
        ("Queue", "Bullseye", "Outer ring", "Either a lower proficiency group or a removed skill.", "Pick the WEM-safe style if you forecast"),
    ],
    [
        q("Proficiency changes who wins under which evaluation?", "Best available skills", ["All skills matching", "Disregard skills", "Neither"], "All-skills uses presence of the tag and idle time."),
        q("An unused extra skill on an agent:", "Does not satisfy a different required skill", ["Counts as any skill", "Deletes utilization", "Publishes the flow"], "The interaction’s required set is what matters."),
        q("The WEM-friendly bullseye expansion is:", "Same skill, lower proficiency group", ["Delete the skill from the org", "Disregard skills", "Turn off On Queue"], "The bullseye overview says this stays compatible with forecasting."),
        q("Inactive agents are excluded based on:", "The previous 7 days of activity", ["Their division name", "Their license only", "Their phone model"], "The evaluation article states the 7 day window."),
        q("All skills matching and a proficiency of 1 versus 5, both holding the tag:", "Idle time decides", ["5 always wins", "1 always wins", "The call disconnects"], "Proficiency is not the sort."),
        q("Skills are stored on:", "The agent profile, and required by the interaction or queue rules", ["The SIP trunk", "The login host", "The fair use table"], "Profiles hold the tags. Routing asks for them."),
    ],
    [("Tag vs number", "All-skills cares about the tag. Best-available cares about the number."), ("7 days", "Inactive agents drop out."), ("WEM style", "Lower proficiency, same skill."), ("Extra skills", "Do not impersonate the required one.")],
    "Assign two proficiencies",
    ["Create the skill name.", "Assign 5 and 2 to two agents.", "Say who wins under all-skills if the 2 is longer idle.", "Say who wins under best-available."],
    "The method and the numbers agree.",
    ("Skill on the queue only", "Admins added a skill requirement and nobody matches.", "Agent profiles: no Billing skill. Queue rule: Billing required. Evaluation: all skills.", "The tag was never assigned.", "Assign Billing to the people who should take the work, or change the evaluation on purpose."),
))

add(lesson(
    "q-acw", "After call work and the system wrap-up codes", "Core", 13,
    "ACW is optional, discretionary, or time-boxed. The platform has its own codes when agents do not finish.",
    [
        "Optional ACW lets the agent skip wrap-up. Mandatory discretionary lets them end ACW themselves. Mandatory time-boxed caps the duration. If Optional or Mandatory discretionary is on, the interaction stays open until the agent ends it. If they log off or close the browser during ACW, it stays open unless you enable End Interactions Automatically when Agents Logoff, which closes it with ININ-SYSTEM-LOGOUT.",
        "If the timer expires before a required code is chosen, Genesys Cloud assigns ININ-WRAP-UP-TIMEOUT. Callbacks require a wrap-up code even when ACW is Optional. Agents can save codes and notes only if they actually enter ACW. A direct transfer can still force a code from the previous queue’s list. Outbound dialing has its own codes. The article says not to use the agent-requested option on outbound campaigns because agents can skip the work the campaign needs.",
    ],
    cites("queues"),
    fig("The segment ends in a code, or the platform writes one.", [
        ("talk", "Talk", "phone", 16, 40),
        ("acw", "ACW", "agent", 46, 40),
        ("code", "Code", "wem", 76, 40),
    ], [("talk", "acw"), ("acw", "code")]),
    "Close the segment on purpose",
    [
        ("Queue", "ACW", "Choose a mode", "Optional, discretionary, or time-boxed.", "Know which one you picked"),
        ("Agent", "Code", "Select", "Required modes will not close without it.", "Notes save only inside ACW"),
        ("Timer", "Platform", "ININ-WRAP-UP-TIMEOUT", "The platform fills the blank.", "You will see it in reports"),
        ("Logoff", "Platform", "ININ-SYSTEM-LOGOUT", "Only if the org setting is on.", "Otherwise ACW sits open"),
        ("Callback", "Rule", "Always a code", "Optional ACW does not waive it.", "The article is specific"),
    ],
    [
        q("ININ-WRAP-UP-TIMEOUT means:", "The ACW timer expired before a code was chosen", ["The trunk failed", "The agent picked a custom code", "Predictive routing turned off"], "The queue article names that system code."),
        q("ININ-SYSTEM-LOGOUT is applied when:", "The org setting closes interactions on logoff during ACW", ["Every normal wrap-up", "A bullseye ring opens", "A token expires"], "It is the logoff path, not the timer path."),
        q("Callbacks and Optional ACW:", "A wrap-up code is still required", ["No code is required", "Callbacks skip the queue", "Callbacks delete the recording"], "The article calls this out."),
        q("Notes and codes are saved when:", "The agent requested ACW and entered it", ["The call connected", "The flow published", "The DID was purchased"], "Skipping ACW skips the save."),
        q("Mandatory time-boxed ACW:", "Caps how long wrap-up can last", ["Removes wrap-up codes", "Sets utilization to 4", "Disables alerting"], "The mode is a maximum duration."),
        q("The article’s warning on outbound campaigns is:", "Do not use the agent-requested option, because agents can skip work the campaign needs", ["Always use it", "It is required for BYOC", "It sets the 80/20 split"], "That warning is in the wrap-up section."),
    ],
    [("Optional", "Agent may skip."), ("TIMEOUT", "Timer won."), ("LOGOUT", "Logoff setting won."), ("Callbacks", "Always need a code.")],
    "Pick an ACW mode",
    ["Choose a mode and say what the agent must do.", "Name both system codes.", "Say what callbacks do under Optional.", "Say why outbound agent-requested is discouraged."],
    "The mode and the two system codes are in your notes.",
    ("Stuck ACW", "Agents who shut the laptop leave interactions open for hours.", "ACW: Mandatory discretionary. End on logoff: off.", "The article says the interaction waits for the agent unless that setting is on.", "Enable End Interactions Automatically when Agents Logoff, and expect ININ-SYSTEM-LOGOUT on those segments."),
))

add(lesson(
    "q-wrapdiv", "Wrap-up codes live in divisions too", "Core", 11,
    "The codes an agent sees are the codes their role can see, and Genesys wants them in the queue’s division.",
    [
        "The queue article says you add wrap-up codes that your role can see, and it recommends codes assigned to the same division as the queue so reports make sense. A code in another division is a reporting split even if an admin with broad access managed to attach it.",
        "Internal calls made on behalf of a queue can hand the receiving agent that queue’s ACW settings and codes. The article’s escape is to place a direct internal call instead of calling on behalf of the queue. The receiving agent may still see the interaction as ACD. Read that note before you debug “wrong code list” on an internal consult.",
    ],
    cites("queues", "divisions"),
    fig("Codes and the queue should share a division.", [
        ("code", "Code", "wem", 22, 40),
        ("div", "Division", "region", 50, 40),
        ("q", "Queue", "queue", 78, 40),
    ], [("code", "div"), ("q", "div")]),
    "Attach codes the report can explain",
    [
        ("Admin", "Codes", "Create in the queue’s division", "Same division as the queue.", "Recommended by the article"),
        ("Admin", "Queue", "Add", "You only see codes your role allows.", "Filter by name to review"),
        ("Agent", "ACW", "Pick", "The list is the queue’s list.", "A transfer can carry the previous queue’s list"),
        ("Agent", "Internal", "Direct call", "Avoid inheriting another queue’s ACW by accident.", "On-behalf calls inherit"),
    ],
    [
        q("Genesys recommends wrap-up codes be assigned to:", "The division the queue belongs to", ["All divisions always", "No division", "The trunk"], "So reports that include the code stay understandable."),
        q("An admin sees codes:", "In divisions their role can access", ["From every customer", "Only system codes", "Only ININ-WRAP-UP-TIMEOUT"], "The picker is permissioned."),
        q("A direct transfer to a user who is not in a queue can still:", "Force a code from the previous segment’s queue", ["Delete the recording", "Change the AWS region", "Skip ACW always"], "The article describes that inheritance."),
        q("Calling on behalf of a queue versus a direct internal call:", "On-behalf inherits that queue’s ACW. Direct is the documented way to avoid it.", ["They are identical", "Direct calls are forbidden", "On-behalf uses RTP only"], "The article draws that distinction."),
        q("Removing a code from the queue:", "Takes it off that queue’s list. It does not have to delete the code object.", ["Deletes the division", "Publishes every flow", "Resets utilization"], "The article has a remove step on the queue list."),
        q("System codes and custom codes:", "Both can appear. System codes are written by the platform in the cases already covered.", ["System codes are illegal", "Custom codes are CX 4 only", "Neither is reported"], "TIMEOUT and LOGOUT are the system examples."),
    ],
    [("Same division", "Queue and codes."), ("Role", "Limits the picker."), ("On behalf", "Inherits ACW."), ("Direct internal", "The documented escape.")],
    "Place codes with the queue",
    ["Name the division.", "Name three codes.", "Say who can see them.", "Say what an on-behalf internal call will inherit."],
    "The code list belongs to the same division as the queue.",
    ("Split report", "Half the wrap-up codes do not filter with the EMEA queue.", "Queue division: EMEA. Codes created in Home and attached by an All-division admin.", "The article’s reporting recommendation was skipped.", "Recreate or move the codes into EMEA and attach those."),
))

add(lesson(
    "q-sl", "Service level is a percentage and a target in seconds", "Core", 11,
    "Each media has a service level percentage and a target duration. That pair is what conditional routing and WFM both mean by “the goal.”",
    [
        "The queue article tells you to set a service level percentage and a service level target in seconds per channel. Voice, chat, email, message, and callback are configured on their own media panels. A single number for “the queue” is not how the admin page works. A voice target of 20 seconds and an email target of an hour can both be honest.",
        "Conditional group routing’s KPI is only meaningful if this pair exists and you believe it. WEM service goal templates, covered in the WFM track, are the planning version of the same idea. Do not set the queue target to 1 second to “look good.” The percentage will tell on you.",
    ],
    cites("queues", "routing", "wem"),
    fig("Percentage answered inside a target, per media.", [
        ("v", "Voice 20s", "phone", 22, 40),
        ("e", "Email", "crm", 55, 40),
        ("goal", "Goal", "wem", 82, 40),
    ], [("v", "goal"), ("e", "goal")]),
    "Set two different targets",
    [
        ("Admin", "Voice", "80 percent in 20 seconds", "A classic voice pair.", "Enter it on the voice panel"),
        ("Admin", "Email", "A longer target", "Email is not voice.", "Own percentage, own seconds"),
        ("Routing", "Conditional", "Use the voice goal", "The donor rule needs a real KPI.", "A blank target protects nothing"),
        ("WFM", "Template", "Plan to the same number", "Forecasts and the queue should not disagree.", "WEM track covers templates"),
    ],
    [
        q("Service level on a queue is:", "A percentage and a target duration, per media", ["A single org-wide millisecond", "A SIP response", "A token count"], "The queue article configures both, by channel."),
        q("Voice and email should share one target because they are one queue?", "No. Each media has its own settings.", ["Yes", "Only on CX 1", "Only if bullseye is off"], "The article has separate channel configuration."),
        q("Conditional routing without a believable service level:", "Has no KPI to protect the donor queue", ["Runs faster", "Disables utilization", "Publishes flows"], "The rule is a KPI plus availability."),
        q("A 1 second voice target will likely:", "Show a poor percentage, because agents cannot answer that fast", ["Guarantee CX 4", "Disable alerting", "Remove skills"], "The percentage is measured against the target you typed."),
        q("Alerting timeout and service level target are:", "Different timers. Alerting is 7–59 seconds for the agent. The target is the caller’s goal.", ["The same field", "Both 72 hours", "Both OAuth settings"], "Do not copy one into the other without reading both."),
        q("WEM service goal templates relate to this number as:", "The planning side of the same service idea", ["A replacement for SIP", "A recording policy", "A login host"], "The WEM article lists service goal templates among planning objects."),
    ],
    [("Pair", "Percentage and seconds."), ("Per media", "Voice is not email."), ("Routing", "Conditional rules need the KPI."), ("WEM", "Templates should agree with the queue.")],
    "Write two targets",
    ["Voice percentage and seconds.", "Email percentage and seconds.", "Say which one a conditional rule would watch.", "Say why 1 second is a bad voice target."],
    "The two medias do not share a fantasy number.",
    ("One number for everything", "Email service level is red every day. Agents answer email in 30 minutes, which leadership said was fine.", "Email target copied from voice: 20 seconds.", "The media panel was not edited.", "Set the email target to the promise you actually made."),
))

add(lesson(
    "q-callback", "Callbacks are interactions with their own rules", "Core", 12,
    "A callback is queued work. It still needs a wrap-up code, and it counts as its own utilization slot.",
    [
        "CX 1 includes callbacks. The utilization default is one callback, and preview calls are treated as callbacks. Calls and callbacks do not interrupt each other by default, so an agent on a live call is not also offered a callback. The queue’s callback media panel has its own service level.",
        "The wrap-up article says a callback requires a wrap-up code even if voice ACW is Optional. Preferred-agent behavior also notes that for email, messaging, and inbound callbacks the platform no longer routes to the last handling agent, while scheduled callbacks are a different case. Read that sentence on the preferred-agent page before you promise “the same agent will call back.”",
    ],
    cites("overview", "util", "queues", "preferred"),
    fig("A callback waits beside voice and consumes its own slot.", [
        ("cust", "Customer", "phone", 14, 40),
        ("cb", "Callback", "queue", 46, 40),
        ("ag", "Agent", "agent", 78, 40),
    ], [("cust", "cb"), ("cb", "ag")]),
    "Offer a callback without double-alerting",
    [
        ("Flow", "Queue", "Create callback", "CX 1 includes the feature.", "It is queued work"),
        ("ACD", "Agent", "One slot", "Default capacity is one callback.", "It will not interrupt a live call by default"),
        ("Agent", "ACW", "Code required", "Even if voice ACW is Optional.", "The article is explicit"),
        ("Design", "Last agent", "Do not promise", "Inbound callbacks are called out on the preferred page.", "Scheduled callbacks are the exception to re-read"),
    ],
    [
        q("Default callback utilization is:", "1", ["4", "0", "Unlimited"], "The utilization article lists one callback."),
        q("A live call and a callback interrupting each other is:", "Off by default", ["Required", "Only in bullseye", "Only for bots"], "The article prevents that interrupt by default."),
        q("Preview calls count as:", "Callbacks", ["Emails", "Workitems", "Chats"], "The utilization article says so."),
        q("Wrap-up on a callback when ACW is Optional:", "Still required", ["Skipped", "Replaced by a token", "Forbidden"], "The queue article says the code is required regardless."),
        q("CX package that includes callbacks in the overview’s voice list:", "CX 1", ["Only CX 4", "Only AppFoundry", "None"], "Callbacks are in the CX 1 description."),
        q("Promising the same agent on every inbound callback is risky because:", "The preferred-agent article says inbound callbacks are no longer routed to the last handling agent", ["Callbacks have no queue", "Agents cannot be On Queue", "RTP forbids it"], "Re-read scheduled versus inbound on that page."),
    ],
    [("Slot", "One callback by default."), ("No interrupt", "Calls and callbacks stay apart."), ("Code", "Required even if ACW is Optional."), ("Last agent", "Do not promise it for inbound callbacks.")],
    "Write the callback rules",
    ["State the utilization default.", "State the interrupt default.", "State the wrap-up rule.", "State what you will not promise about the same agent."],
    "The callback design does not contradict the three articles.",
    ("Double alert", "Agents on live calls also get callback alerts and miss both.", "Interrupt: calls may interrupt callbacks, and callbacks may interrupt calls. An admin enabled both.", "The default was changed.", "Restore the default that keeps calls and callbacks from interrupting each other, unless you have a measured reason not to."),
    "Scheduled callbacks are called out separately from inbound callbacks on the preferred-agent page. Confirm the current sentence before you design a scheduled campaign around last-agent behavior.",
))

add(lesson(
    "q-members", "Membership, On Queue, and the copy trap", "Core", 11,
    "A copied queue can duplicate a bullseye you did not mean to clone.",
    [
        "Membership is the list of agents who may receive the queue’s work, up to 5,000. On Queue is the status that actually enters them. Copying settings and members is a shortcut and a trap: routing method, evaluation, bullseye rings, wrap-up, and ACW come along. The article says you can edit after the copy. Do that before the queue takes a DID.",
        "An agent in the member list who is off queue, fully utilized, or missing a required skill under all-skills matching will not be offered the interaction. The simulator makes those three filters obvious. Production adds the 7 day activity window and the scoring across queues.",
    ],
    cites("queues", "evaluation", "util"),
    fig("Members are the roster. On Queue is the door.", [
        ("list", "Members", "queue", 22, 40),
        ("on", "On Queue", "agent", 55, 22),
        ("off", "Off queue", "agent", 55, 68),
    ], [("list", "on")]),
    "Copy, then edit, then test",
    [
        ("Admin", "Copy", "From Billing", "Members and settings arrive together.", "Open the routing tab"),
        ("Admin", "Rings", "Reset if needed", "A five-ring plan may not fit the new queue.", "Evaluation too"),
        ("Agent", "Status", "On Queue", "Membership is not enough.", "Off queue is invisible"),
        ("Test", "Call", "One agent", "Confirm who is offered.", "Then add the DID"),
    ],
    [
        q("Copying a queue copies:", "Settings and members, including routing if that is part of the configuration", ["Only the name", "Only the division’s login host", "Nothing"], "The article says settings and members, and you can edit after."),
        q("An off-queue member is:", "Not offered ACD interactions", ["The first choice", "Automatically preferred", "A trunk"], "On Queue is the entry status."),
        q("The member cap still applies to a copied queue:", "Yes. 5,000.", ["No", "The cap becomes 10,000", "The cap is 200"], "The limit is per queue."),
        q("Fully utilized members are:", "Skipped", ["Preferred", "Given a second voice call by default", "Moved to Home"], "Utilization removes them from the offer."),
        q("The 7 day activity rule means a copied roster can include:", "People who will not be selected until they are active again", ["Only bots", "Only CX 4", "Only preferred agents"], "The evaluation article excludes inactive agents."),
        q("The right time to attach a DID is:", "After you have reviewed routing and placed a test call", ["Before the queue exists", "During the copy dialog only", "After deleting Home"], "A copied bullseye should be a choice, not a surprise."),
    ],
    [("Copy", "Review routing immediately."), ("On Queue", "The door."), ("5,000", "Still the cap."), ("Test", "Before the DID.")],
    "Review a copied queue",
    ["List three settings you will reopen.", "Confirm member count under 5,000.", "Name the status agents must select.", "Place a test before cutover."],
    "The copy is a draft, not a launch.",
    ("Inherited rings", "A new overflow queue waits 72 hours on ring 1 because the source was a specialty queue.", "Copied bullseye delay: 259200 seconds.", "The maximum delay was copied on purpose in the source and by accident here.", "Set a delay that matches this queue’s promise, publish nothing else until a test call expands the way you expect."),
))
