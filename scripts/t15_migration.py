from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "migration",
    "title": "Migration",
    "kicker": "Rebuild",
    "accent": 1,
    "summary": "Engage, PureConnect, and Cisco UCCE move by rebuilding Architect flows and queues. This is a learning bridge, not a converter.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "x-rebuild", "Nothing imports your old routing by magic", "Core", 12,
    "You rebuild flows, queues, and trunks. You do not flip a converter this lab has not found.",
    [
        "Genesys Engage routing strategies and PureConnect handlers do not become Architect flows because a project plan says “migrate”. This lab has not found a documented one-click import. The work is to redraw the caller journey in Architect, recreate queues, and point numbers at the new routes. The migration studio in this lab is a table of those mappings, not a tool that edits either platform.",
        "Cisco UCCE, UCCX, and a CUCM or Webex Calling trunk are a different vendor. The bridge lessons cite Cisco’s product pages for what you are leaving and Genesys articles for what you are building. They are not a statement that the platforms are equivalent.",
    ],
    cites("architect", "queues", "create-flow", "ucce"),
    fig("Old logic is read. New flows are written. The table does not convert.", [
        ("old", "Old platform", "crm", 16, 40),
        ("map", "Bridge", "architect", 48, 40),
        ("new", "Architect", "queue", 82, 40),
    ], [("old", "map"), ("map", "new")]),
    "Start with a journey, not an object dump",
    [
        ("Caller", "One path", "Write it in sentences", "What they hear, where they queue.", "Ignore object names at first"),
        ("Architect", "Flows", "Inbound, in-queue, modules", "Publish them.", "Drafts do not answer"),
        ("ACD", "Queues", "Members, skills, methods", "Create-queues article.", "5000 members, one division"),
        ("Numbers", "Routes", "Last", "After the path works.", "Emergency included"),
    ],
    [
        q("A documented one-click import of old routing into Architect:", "Is not something this lab found. Plan to rebuild.", ["Is the default", "Is an Edge firmware", "Is GC-GCP"], "The studio says rebuild."),
        q("The migration studio:", "Maps concepts. It does not call either platform.", ["Converts IRD files", "Pushes to UCCE", "Buys DIDs"], "It is a table."),
        q("The first artifact is:", "The caller journey in sentences", ["A trunk ACL", "A token budget", "An exam voucher"], "Objects come after."),
        q("Queues in the new org still follow:", "Unique names, one division, the member limit", ["UCCE’s database", "No rules", "Implicit grant"], "The create-queues article."),
        q("Cisco pages in this track are:", "The source for the platform you are leaving", ["Genesys articles", "Optional fiction", "RFCs"], "Do not cite them as Genesys behavior."),
        q("Unpublished Architect flows during cutover:", "Do not answer calls", ["Run as drafts", "Use the old IVR automatically", "Set utilization"], "Publish."),
    ],
    [("Rebuild", "The default."), ("Studio", "A map, not a converter."), ("Journey", "Sentences first."), ("Publish", "Or it does not run.")],
    "Pick one journey",
    ["Write five sentences a caller would recognize.", "Name the Architect flow types.", "Name the queue.", "Name what you will not automate."],
    "The last line says rebuild, not import.",
    ("Ghost converter", "The plan says the IRD will be imported on Friday. Nobody owns an Architect flow.", "No published inbound flow. Cutover in two days.", "The converter was a rumor.", "Assign the rebuild. Delay cutover until the flow is published and called."),
    "Lifecycle dates for Engage and PureConnect must be confirmed on Genesys notices. This lesson does not set one.",
))

add(lesson(
    "x-engage", "Engage and PureConnect become flows and queues", "Core", 12,
    "Strategies, IRDs, and handlers are read as behavior, then redrawn.",
    [
        "Treat a Genesys Engage routing strategy or IRD as a description of menus, data dips, and targets. Treat PureConnect handlers and queues the same way. The Genesys Cloud objects are Architect flows, including common modules for anything you would otherwise paste twice, and queues with skills and a routing method. Confirm the current PureConnect or Engage lifecycle on a Genesys notice before you put a date in a steering deck. Community dates are not a contract.",
        "Recording policies, WFM, and bots do not come along inside the IVR export. They are separate tracks in this lab because they are separate products. A cutover that only moves prompts has not moved the contact center.",
    ],
    cites("architect", "create-flow", "queues", "wem"),
    fig("Strategy in, modules and queues out.", [
        ("ird", "Strategy", "crm", 14, 40),
        ("mod", "Modules", "architect", 48, 22),
        ("q", "Queues", "queue", 48, 68),
        ("wem", "WEM", "wem", 82, 40),
    ], [("ird", "mod"), ("ird", "q"), ("q", "wem")]),
    "Translate one strategy",
    [
        ("Read", "Prompts", "Architect audio", "Not a binary paste.", "Secure flows if you collect digits"),
        ("Read", "Targets", "Queues and skills", "Not a single mega-queue unless you mean it.", "Routing method explicit"),
        ("Read", "Shared logic", "Common modules", "One holiday check, not twelve copies.", "Publish the module"),
        ("Date", "Notice", "Genesys lifecycle", "Confirm it.", "No community EOL in the deck"),
    ],
    [
        q("An Engage strategy maps to:", "Architect behavior you redraw", ["A phone trunk automatically", "A Cisco script", "An OAuth grant"], "Rebuild."),
        q("PureConnect handlers map to:", "Architect flows, and their queues map to Genesys Cloud queues", ["Edge groups only", "STA topics only", "Nothing"], "Both objects matter."),
        q("A lifecycle date in the steering deck must come from:", "A Genesys notice you opened", ["A forum", "This lab’s memory", "A Cisco page"], "Mark it unconfirmed until then."),
        q("Shared holiday logic belongs in:", "A common module", ["Twelve copied tasks", "A number plan", "SCIM"], "The Architect track explains why."),
        q("WFM after cutover:", "Is a separate workstream", ["Hides inside the IVR export", "Is free with any queue", "Is an RFC"], "CX 3 on the overview."),
        q("Digit collection that used to be recorded:", "Needs a secure-flow decision again", ["Is safe by default", "Is a topic", "Is bullseye"], "Do not copy digits into participant data."),
    ],
    [("Strategy", "Behavior, not a file format."), ("Queues", "Recreated."), ("Date", "A Genesys notice."), ("WEM", "Its own workstream.")],
    "List what the export will not do",
    ["Prompts you must re-record or re-point.", "Queues you must recreate.", "WFM objects.", "The lifecycle page you still need."],
    "The lifecycle item says “confirm”, not a date.",
    ("Forum EOL", "The deck says PureConnect ends on a date copied from a blog.", "No Genesys notice in the packet.", "The date is not a source.", "Replace it with a link to the notice, or mark it unknown."),
    "Do not treat WarmTransfer or any third-party blog as Genesys’ lifecycle notice.",
))

add(lesson(
    "x-ivr", "IVR becomes Architect tasks, menus, and audio", "Core", 12,
    "CVP, UCCX prompts, and Engage voice all become the same kind of flow.",
    [
        "Create a flow is the article for the voice tasks you will rebuild: play audio, collect input, decisions, transfers, data actions. Cisco’s UCCX and UCCE pages remain the description of the old script. The mapping is conceptual. A CVP application and a UCCX script both become Architect if the journey is a voice menu. They do not keep their tool names.",
        "In-queue treatment is a separate flow type, and the default in-queue call flow does nothing until you publish it. Migrating “music on hold” is not done when the inbound menu works. Call the queue and sit in it.",
    ],
    cites("create-flow", "inqueue", "uccx", "ucce"),
    fig("Old IVR tools collapse into Architect tasks.", [
        ("cvp", "CVP", "phone", 14, 28),
        ("uccx", "UCCX", "phone", 14, 62),
        ("arch", "Architect", "architect", 55, 40),
        ("inq", "In-queue", "queue", 86, 40),
    ], [("cvp", "arch"), ("uccx", "arch"), ("arch", "inq")]),
    "Rebuild the menu and the hold",
    [
        ("Menu", "Collect", "Architect collect input", "DTMF follows the audio article’s model.", "RFC 4733 is the telephony backdrop, not the admin guide"),
        ("Data", "Dip", "Data action", "Timeout and a failure output.", "CRM is not the IVR"),
        ("Hold", "In-queue", "Publish it", "Music action, no menus.", "Default is not live"),
        ("Test", "Call", "Both paths", "A menu choice and a wait.", "Two tests"),
    ],
    [
        q("CVP and a UCCX voice script both become:", "Architect flows you write again", ["Edge groups", "OAuth clients automatically", "The same XML file"], "The tool name does not survive."),
        q("Music on hold in Genesys Cloud is:", "An in-queue flow you publish", ["Automatic because the inbound flow exists", "A trunk setting only", "A topic"], "Call the queue and wait."),
        q("A data dip in the old IVR becomes:", "A data action with a failure path", ["A skill", "A division", "A cert"], "Do not block forever."),
        q("Cisco’s scripting guides are cited to:", "Describe the system you are leaving", ["Replace help.genesys.cloud", "Set token prices", "Define E.164"], "Keep the vendors apart."),
        q("The default in-queue call flow:", "Exists and is not auto-published", ["Is live at org create", "Cannot play audio", "Is a bot"], "Publish it."),
        q("DTMF design still has to respect:", "What Architect collects, with telephony standards in the background", ["Only the UCCE precision queue", "Only sentiment", "Only SCIM"], "Test digits."),
    ],
    [("Menu", "Architect tasks."), ("Hold", "Published in-queue flow."), ("Dip", "Data action plus failure."), ("Cisco", "Source of the old behavior only.")],
    "Two test calls",
    ["The menu choice.", "The hold.", "The data-action failure.", "Which old script you are not importing."],
    "Both test calls are written as scripts a tester can run.",
    ("Menu only", "Agents answer, then silence, because hold was never published.", "Inbound flow: published. In-queue: default, not published.", "The journey was half rebuilt.", "Publish the in-queue flow and call it."),
))

add(lesson(
    "x-ucce", "UCCE skill groups and precision queues are not Genesys queues", "Core", 13,
    "Membership, skills, and bullseye are three ideas you reassemble.",
    [
        "Cisco’s UCCE pages describe skill groups and precision queues as that product’s targeting. In Genesys Cloud a queue has members, and skills sit on the agents. All-skills matching, best available, and disregard skills are evaluation methods. Bullseye adds up to five rings, a delay from 2 seconds to 72 hours, and removal of up to 50 skills. Preferred agents are a further method. None of these objects is a UCCE skill group.",
        "A precision queue that expands over time is the closest teaching analogy to bullseye. It is an analogy. The limits above are Genesys settings. Quote Cisco’s guide for Cisco’s limits, not these.",
    ],
    cites("ucce", "routing", "bullseye", "evaluation"),
    fig("Skill group becomes members plus skills. Precision queue suggests bullseye.", [
        ("sg", "Skill group", "crm", 14, 28),
        ("pq", "Precision", "crm", 14, 68),
        ("mem", "Members", "queue", 55, 28),
        ("eye", "Bullseye", "architect", 55, 68),
    ], [("sg", "mem"), ("pq", "eye")]),
    "Rebuild one target",
    [
        ("Skill group", "Queue", "Members who should answer", "Plus skills if you need them.", "Not the group name alone"),
        ("Precision", "Rings", "If the old queue expanded", "Map steps to rings.", "Max five"),
        ("Eval", "All or best", "Write it down", "Longest idle versus proficiency.", "Disregard is a choice"),
        ("Test", "Offer", "The simulator in this lab", "Then a real queue.", "Teaching model, not the router"),
    ],
    [
        q("A UCCE skill group maps most honestly to:", "Queue membership, plus skills if the old group used them", ["A single SIP header", "An OAuth client", "A recording policy"], "It is not one Genesys object."),
        q("Bullseye’s documented ring count is:", "Up to 5", ["Up to 50", "Exactly 2", "Unlimited"], "50 is the skill-removal cap, not the ring cap."),
        q("Ring delay can be:", "2 seconds to 259200 seconds", ["Only 8 seconds", "Only 30 minutes", "Negative"], "72 hours is the top of that range."),
        q("Precision-queue steps and bullseye rings are:", "A teaching analogy with different limits", ["The same database", "Both Cisco", "Both deprecated"], "Do not copy numbers across vendors."),
        q("Best available skills evaluates:", "The 100 longest-idle matches, then average proficiency", ["Only preferred agents", "Only the newest agent", "Only supervisors"], "The evaluation article."),
        q("This lab’s routing simulator is:", "A teaching model", ["The production router", "UCCE", "A converter"], "Use it to learn, then test in the org."),
    ],
    [("Members", "Who may answer."), ("Skills", "What they must match."), ("Rings", "Up to five."), ("Analogy", "Not a converter.")],
    "Map one precision queue",
    ["The old steps.", "The Genesys rings, five or fewer.", "The evaluation method.", "A test that a preferred agent still wins when the article says they should."],
    "The ring count is five or fewer.",
    ("Fifty rings", "The design has one ring per UCCE step and runs past five.", "Steps: 9. Bullseye max: 5.", "The analogy ignored the cap.", "Collapse steps to five rings or fewer, and document what you merged."),
))

add(lesson(
    "x-uccx", "UCCX is a smaller center with the same rebuild rule", "Core", 11,
    "Scripts, CSQs, and the Finesse desktop do not move as files.",
    [
        "Cisco’s UCCX series page is the door to that product’s scripts, contact service queues, and agent desktop. In Genesys Cloud the script becomes Architect, the CSQ becomes a queue with members and skills, and the desktop becomes the Genesys workspace or a documented CRM embed such as Salesforce or Zendesk. Finesse gadgets do not install from AppFoundry under a new name unless a listing you open says so.",
        "UCCX customers often have a single site and a CUCM. The trunk lesson is next. Do not start with the trunk. Start with one published flow and one queue, then call it with a test number.",
    ],
    cites("uccx", "create-flow", "queues", "salesforce"),
    fig("Script, CSQ, and desktop split into three Genesys decisions.", [
        ("sc", "Script", "phone", 14, 40),
        ("ar", "Architect", "architect", 48, 22),
        ("q", "Queue", "queue", 48, 55),
        ("desk", "Desktop", "agent", 82, 40),
    ], [("sc", "ar"), ("sc", "q"), ("sc", "desk")]),
    "Split the UCCX site",
    [
        ("Script", "Flow", "Rebuild", "Publish.", "No XML import in this lab"),
        ("CSQ", "Queue", "Members and skills", "One division.", "Routing method chosen"),
        ("Desktop", "Workspace or CRM", "Salesforce or Zendesk if that is the requirement", "Cite the article.", "Do not promise Finesse parity"),
        ("Call", "Test", "Before the trunk cut", "A test number.", "Hear the flow"),
    ],
    [
        q("A UCCX script becomes:", "An Architect flow you publish", ["A firmware image", "A client-credentials token", "A topic program"], "Rebuild."),
        q("A CSQ is closest to:", "A Genesys queue", ["A login host", "A satellite region", "An implicit grant"], "Add skills only if you need them."),
        q("Finesse gadgets:", "Are not assumed to exist on AppFoundry", ["Install automatically", "Are Dialog Engine bots", "Are number plans"], "Open the listing if you need one."),
        q("The desktop choice this lab will cite is:", "The Genesys workspace, or Salesforce or Zendesk when those articles match", ["Always Finesse", "Always Dynamics", "A personal mailbox"], "No invented CRM."),
        q("The first test should happen:", "Before you cut the production trunk", ["After you delete CUCM", "Only in production", "Only after GC-GCP"], "Hear the flow."),
        q("UCCX and UCCE in this lab are:", "Both Cisco sources, with different pages", ["The same product", "Both Genesys", "Both deprecated by RFC"], "Cite the series you mean."),
    ],
    [("Script", "Architect."), ("CSQ", "Queue."), ("Desktop", "Workspace or a cited embed."), ("Test", "Before the trunk cut.")],
    "Write the UCCX row",
    ["One script.", "One CSQ.", "The desktop decision.", "The test number’s job."],
    "Finesse is not in the desktop decision unless you found a listing.",
    ("Gadget hope", "Agents expect their Finesse gadget on day one. Nothing was installed.", "No AppFoundry install. Workspace unconfigured.", "Parity was assumed.", "Pick the workspace or a documented embed and train to that."),
))

add(lesson(
    "x-cucm", "CUCM stays. BYOC is the door, not a replacement cluster.", "Core", 12,
    "A dial plan and a trunk are Genesys number plans and a BYOC trunk. CUCM is still yours.",
    [
        "The migration studio’s CUCM row points at BYOC PBX or BYOC Carrier, and at Dynamic Cloud Voice for new cloud trunks. Genesys does not absorb the CUCM cluster. Extensions, partitions, and calling search spaces stay on the Cisco side until you deliberately move a pattern. Number plans on the Genesys site classify what Genesys sees, up to 200 plans per site, including the emergency classification.",
        "Local route groups and a premises Edge are a different design from a cloud trunk. If phones register to an Edge, use the Edge track. If CUCM sends a SIP trunk to Genesys, use the BYOC track. Do not draw both and configure neither.",
    ],
    cites("byoc", "dcvp", "numbers", "edges"),
    fig("CUCM remains. A trunk crosses. Number plans classify.", [
        ("cu", "CUCM", "phone", 16, 40),
        ("tr", "BYOC", "trunk", 50, 40),
        ("np", "Plans", "architect", 82, 40),
    ], [("cu", "tr"), ("tr", "np")]),
    "Choose the door",
    [
        ("Cloud", "SIP to Genesys", "BYOC Cloud", "New trunks: Dynamic Cloud Voice.", "ACL the documented egress, do not copy a stale list"),
        ("Premises", "Phones on an Edge", "Edge group", "Local site routing.", "Different track"),
        ("Plans", "Emergency", "Before the DID cut", "911 and the site’s country.", "Genesys is not the emergency provider on BYOC"),
        ("Test", "One pattern", "A lab extension", "Not the operator route.", "Then expand"),
    ],
    [
        q("CUCM after a Genesys deployment:", "Still exists unless you have a separate plan to remove it", ["Is deleted by BYOC", "Becomes an Edge", "Becomes Architect"], "The cluster is yours."),
        q("New BYOC Cloud trunks should use:", "Dynamic Cloud Voice", ["A copied 2019 IP list", "Implicit grant", "A precision queue"], "The DCVP article is the current platform."),
        q("Number plans:", "Classify dialed strings on the Genesys site, up to 200 per site", ["Replace CUCM partitions automatically", "Are topics", "Are tokens"], "Emergency is one classification."),
        q("Phones that must stay local to a site point at:", "A premises Edge design", ["Only a cloud trunk with no Edge", "SCIM", "A bot"], "Pick one door and finish it."),
        q("BYOC emergency calling:", "Requires the emergency setup article, and Genesys is not the provider", ["Is automatic worldwide", "Uses 988 as a backup PSAP", "Is a fair-use footnote"], "Do not invent a backup PSAP."),
        q("Copying an old media ACL forward:", "Breaks when ingress addresses change", ["Is the DCVP migration", "Is required", "Is a queue setting"], "Follow the current allowlist guidance."),
    ],
    [("Cluster", "Stays until you remove it."), ("Cloud", "BYOC and DCVP."), ("Edge", "If phones are local."), ("Emergency", "A real test, not a guess.")],
    "Pick the door in writing",
    ["Cloud or premises.", "Who owns CUCM.", "The emergency classification.", "The first lab pattern."],
    "One door is chosen.",
    ("Both doors, neither built", "Cutover weekend has no trunk and no Edge.", "Design: “SIP or Edge, TBD”.", "The choice was deferred until there was no time.", "Choose, configure the lab pattern, and test it the week before."),
))

add(lesson(
    "x-webex", "Webex is a neighbor, not a page this lab pretends to summarize", "Core", 10,
    "Use Cisco’s product pages. Do not cite a Webex help URL this lab did not confirm.",
    [
        "Webex Contact Center and Webex Calling show up in the same migrations as CUCM. This lab did not confirm a specific Webex help article to deep-link, so it will not invent one. Cisco’s UCCE and UCCX series pages are the Cisco citations already checked. For Webex, say “open the current Cisco or Webex document” and attach it in your own design.",
        "Where Webex Calling is the PBX, the Genesys side is still a BYOC trunk or a premises Edge, plus Architect and queues. The neighbor can change its calling model without Genesys’ articles changing. Re-read both sides in the same week.",
    ],
    cites("ucce", "byoc", "architect"),
    fig("Webex stays on Cisco’s side of the bridge.", [
        ("wx", "Webex", "phone", 18, 40),
        ("gap", "Your cite", "architect", 50, 40),
        ("gc", "Genesys", "queue", 82, 40),
    ], [("wx", "gap"), ("gap", "gc")]),
    "Leave a blank you are proud of",
    [
        ("Webex", "Doc", "Attach the page you opened", "Not a link from memory.", "This lab left it blank on purpose"),
        ("Genesys", "Door", "BYOC or Edge", "Already chosen in the previous lesson.", "Do not add a third"),
        ("Journey", "Architect", "Still rebuilt", "The neighbor does not import flows.", "Publish"),
        ("Date", "Both sides", "Re-read the same week", "Products move.", "Uncertainty is allowed"),
    ],
    [
        q("This lab’s Webex help deep link is:", "Absent on purpose", ["help.webex.com/anything", "A Genesys article", "An RFC"], "Confirm your own source."),
        q("Webex Calling as a PBX still needs:", "A Genesys trunk or Edge design", ["Nothing", "Only a bot", "Only STA"], "The neighbor is not the contact center."),
        q("UCCE series pages are cited because:", "They were confirmed Cisco documents", ["They describe Webex Contact Center fully", "They replace Architect", "They set token prices"], "Do not stretch them."),
        q("A design that says “same as CUCM” for Webex:", "Needs a Webex document attached", ["Is automatically true", "Is bullseye", "Is a grant type"], "They are not the same paragraph."),
        q("Architect flows are imported from Webex when:", "They are not. You rebuild.", ["Always", "On CX 1", "If the name matches"], "The rebuild rule stands."),
        q("Re-reading both vendors the same week matters because:", "Either side can change", ["RFCs expire weekly", "Divisions expire", "Queues expire"], "Put the dates in the design."),
    ],
    [("Blank", "Better than a bad link."), ("Door", "BYOC or Edge."), ("Flows", "Rebuilt."), ("Week", "Re-read both sides.")],
    "Attach or abstain",
    ["The Webex document title you personally opened, or the word abstain.", "The Genesys door.", "The flow you will publish.", "The date you will re-read."],
    "Abstain is an acceptable answer.",
    ("Imaginary help center", "The design links a Webex article that opens a generic help home.", "URL not checked.", "The cite is theater.", "Open the article, or remove the link."),
    "No specific Webex Contact Center article was confirmed for this lab. Attach your own.",
))

add(lesson(
    "x-cut", "Cut over one number, then the queue, then the people", "Core", 12,
    "A weekend big-bang is how untested emergency routes meet a full staff.",
    [
        "Order: a lab number through the new trunk or Edge, the emergency classification tested the way the emergency article allows, one published inbound flow, one published in-queue flow, one queue with real agents On Queue, then a single production number. Fair-use and recording policies should already exist, or you will record nothing and be surprised, or record everything and surprise legal.",
        "Rollback is the old route still in place for every number you have not moved. Do not delete the CUCM pattern or the Engage route as the first step. Write the rollback as a person’s action, with a clock time.",
    ],
    cites("emergency", "create-flow", "queues", "recording"),
    fig("Lab number, then one production number, then the rest.", [
        ("lab", "Lab DID", "phone", 14, 40),
        ("one", "One prod", "trunk", 48, 40),
        ("rest", "The rest", "queue", 82, 40),
    ], [("lab", "one"), ("one", "rest")]),
    "Run the narrow cut",
    [
        ("Lab", "Call", "Hear Architect", "And hold music.", "Both flows published"),
        ("Emergency", "Test", "The legal method", "Not a guess at a backup PSAP.", "Before any production DID"),
        ("One", "DID", "Move a quiet number", "Agents On Queue.", "Utilization understood"),
        ("Back", "Who", "Named person and a time", "Old route remains.", "Until you intend to remove it"),
    ],
    [
        q("The first production move should be:", "One number, after a lab call worked", ["Every DID on Friday night", "The emergency route only", "SCIM"], "Narrow cuts."),
        q("Emergency testing happens:", "Before production DIDs move", ["The following quarter", "Only in a slide", "After you delete the old route"], "The emergency track is blunt about this."),
        q("Rollback is:", "A named person restoring the old route", ["Hope", "Deleting Home", "Turning off STA"], "Write the clock time."),
        q("In-queue silence means:", "The hold flow is not published or not selected", ["Bullseye failed", "The cert expired", "Tokens ran out"], "Call it before cutover."),
        q("Recording policy before cutover:", "Decides what you keep on day one", ["Is optional because QM can invent audio", "Is a bot", "Is a grant"], "Set it."),
        q("Deleting the old route first:", "Removes rollback", ["Is best practice", "Is required by RFC 3261", "Publishes flows"], "Leave it until the new path is proven."),
    ],
    [("Lab", "First call."), ("Emergency", "Before the DID."), ("One number", "Then the rest."), ("Rollback", "A person and a clock.")],
    "Write the clock",
    ["Lab call time.", "Emergency test.", "The one production number.", "The rollback owner."],
    "The owner is a name, not “the team”.",
    ("Big bang", "All DIDs move while the in-queue flow is still a draft.", "Change ticket: 400 numbers. In-queue: unpublished.", "The order was reversed.", "Move one number after both flows are published and called."),
))
