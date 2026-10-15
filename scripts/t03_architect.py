from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "architect",
    "title": "Architect flows",
    "kicker": "Design",
    "accent": 3,
    "summary": "Flow types, tasks, in-queue experiences, data actions, bots, secure calls, and publish.",
    "lessons": [],
}
def add(item):
    TRACK["lessons"].append(item)

add(lesson(
    "a-types", "The flow types on the Architect home page", "Core", 13,
    "Architect is a list of flow types. Picking the wrong tab is the first defect.",
    [
        "The home page documents inbound call, inbound message, inbound email, inbound chat, outbound call, bot flow, common module, in-queue call, in-queue email, in-queue message, secure call, voicemail, workflow, and survey invite. The create-a-flow article also names digital bot flows, voice survey, web survey invite, and workitem flows. Names must be unique inside one type, may repeat across types, and may be at most 200 characters.",
        "You need Architect flow permissions to add, edit, and view, plus the routing permissions the flow type requires. Message and email flows ask for an error-event queue. A new flow can take a few seconds to appear. The home page has a refresh for that lag. It is not a failed save.",
    ],
    cites("arch-home", "create-flow"),
    fig("Flow types are siblings. A name can repeat across types, not inside one.", [
        ("in", "Inbound call", "phone", 16, 28),
        ("msg", "Message", "queue", 40, 28),
        ("bot", "Bot", "bot", 64, 28),
        ("cm", "Common module", "architect", 40, 70),
    ], [("in", "bot"), ("in", "cm"), ("msg", "bot")]),
    "Create the right type",
    [
        ("Admin", "Architect", "Choose type", "The tab is the contract.", "Inbound call is not inbound message"),
        ("Admin", "Name", "200 characters", "Unique inside the type.", "Same name may exist on another type"),
        ("Admin", "Division", "Assign", "The flow is a configuration object.", "Access follows the division"),
        ("Admin", "Language", "Default TTS", "Pick a supported language.", "Not a cosmetic label"),
        ("Admin", "Refresh", "See the flow", "Creation can lag.", "Refresh before you assume failure"),
    ],
    [
        q("A flow name may be at most how many characters?", "200", ["50", "32", "Unlimited"], "Create a flow states the 200 character limit."),
        q("Can an inbound call flow and a bot flow share a name?", "Yes. Uniqueness is per flow type.", ["No", "Only in Home", "Only after publish"], "The article allows the same name across types."),
        q("An error-event transfer queue is part of creating which flows?", "Message and email flows", ["Every phone trunk", "Only secure call", "Only surveys"], "The create article calls that field out for message and email."),
        q("Which permission family does create-a-flow require besides routing?", "Architect flow add, edit, and view", ["Only WFM", "Only billing", "Only Edge"], "Those Architect permissions are the prerequisite."),
        q("Workitem flows are documented as:", "A flow type, one flow per worktype in the create article", ["A SIP method", "A satellite region", "A license called EX only"], "The create article includes workitem flows and a one-flow-per-worktype limit."),
        q("The flow does not show up for several seconds. The documented response is:", "Refresh the Architect home list", ["Rebuild the org", "Delete Home", "Change AWS region"], "The article mentions the lag and the refresh control."),
    ],
    [("200", "Maximum flow name length."), ("Per type", "Names are unique inside a type only."), ("Tabs", "Call, message, email, chat, bot, in-queue, secure, workflow, survey, and others."), ("Refresh", "Creation lag is expected.")],
    "Name three flows without colliding",
    ["Pick a call flow name under 200 characters.", "Use the same string on a bot flow and explain why that is legal.", "Try the same string on a second call flow and explain why that is not.", "Note the division you would assign."],
    "You can defend the name and the tab.",
    ("Wrong tab", "A WhatsApp design was built as an inbound call flow.", "Flow type: inbound call. Channel asked for: message.", "Message routing never opens a call flow.", "Create an inbound message flow. Leave the call flow for the DID."),
))

add(lesson(
    "a-task", "Tasks, menus, and a way out", "Core", 13,
    "An inbound call flow plays audio, collects input, and must transfer, hand off, or disconnect.",
    [
        "About Architect describes linking actions: play audio, route to agents, queues, voicemail, numbers, or other flows, collect digits outside a menu, dip data, and branch with expressions. The inbound example in the bot article shows a question, a decision, and a transfer. That shape is the whole product in miniature.",
        "A flow with only Play Audio has no exit. Transfer to ACD needs a real queue. Disconnect needs a reason the caller can understand. Call Bot Flow is an exit only if the bot itself has a failure path back to a queue. Secure flows are a special case covered later. They use a blind transfer rather than a consultation VXML transfer.",
    ],
    cites("architect", "bot-inbound", "create-flow"),
    fig("A task is an ordered list with an exit.", [
        ("play", "Play", "phone", 16, 40),
        ("col", "Collect", "architect", 40, 40),
        ("dec", "Decision", "bot", 62, 40),
        ("acd", "ACD", "queue", 84, 40),
    ], [("play", "col"), ("col", "dec"), ("dec", "acd")]),
    "Billing menu, lab version",
    [
        ("Flow", "Caller", "Play Audio", "Say why the caller reached you.", "Prompt text, not a file you do not own"),
        ("Flow", "Caller", "Collect Input", "One digit is enough for a lab.", "No digit, no branch"),
        ("Flow", "Logic", "Decision", "Branch on the digit.", "Else is required"),
        ("Flow", "Queue", "Transfer to ACD", "The queue must exist.", "Division must be one you can see"),
        ("Flow", "Caller", "Disconnect", "The other branch says goodbye.", "Do not drop the call silently"),
    ],
    [
        q("About Architect says you can route to which destinations?", "Agents, queues, voicemail, external numbers, or other flows", ["Only a bot", "Only FedRAMP", "Only a CSV"], "That list is the product description."),
        q("A task that only plays audio is incomplete because:", "The caller has no route and no disconnect", ["Audio is forbidden", "Play Audio requires CX 4", "SIP forbids prompts"], "Every example in the lab ends in a transfer, a bot, or a disconnect."),
        q("Secure call flows, per the create article, use:", "A blind transfer rather than a consultation VXML transfer", ["A WebRTC phone only", "An email flow", "Predictive routing"], "The article explains the blind transfer as the way to avoid transfer failure."),
        q("Call Data Action belongs in the flow when:", "You need a system outside Genesys during the conversation", ["You need a new AWS region", "You need to delete Home", "You need a concurrent peak"], "Data dips are part of the Architect description."),
        q("The bot article’s banking example asks the caller to:", "Check a balance or find a branch", ["Buy a trunk", "Set a fair-use rate", "Choose a satellite"], "That is the documented template story."),
        q("Transfer to ACD fails closed when:", "The queue name does not exist or you cannot see that division", ["The prompt is polite", "The flow name is 20 characters", "RTP is encrypted"], "The action needs a real queue you are allowed to reference."),
    ],
    [("Actions", "Play, collect, decide, transfer, dip, disconnect."), ("Exit", "Queue, bot, or disconnect."), ("Secure", "Blind transfer, not consultation VXML."), ("Data dip", "A first-class Architect idea.")],
    "Sketch a three-action task",
    ["Write the prompt.", "Write the digit you collect.", "Name the queue for digit 1.", "Write the disconnect phrase for anything else."],
    "Someone else could build the task from your card.",
    ("No else", "Callers who press 2 sit in the flow.", "Decision: equals 1 transfers. No other output.", "Unmatched input has no path.", "Add an else that replays the prompt once and then disconnects or transfers to a general queue."),
))

add(lesson(
    "a-inqueue", "In-queue flows are the hold experience", "Core", 12,
    "The caller is already queued. The in-queue flow is what they hear or read while ACD looks for an agent.",
    [
        "For calls, Architect supplies a default in-queue flow built around a music action. Menus and reusable tasks are not available in that flow type. The default is not published for you. Until you publish it, it does not handle waiting calls. You can replace the music and add actions, then republish.",
        "Email and message do not get a built-in default. You create those in-queue flows and attach them. An outbound email or message does not launch the in-queue flow. It launches when an inbound response arrives. Treat any exact overall timeout you remember as something to re-read on the in-queue article. The page describes those periods and they are easy to mis-quote.",
    ],
    cites("inqueue", "arch-home"),
    fig("ACD searches while the in-queue flow plays.", [
        ("c", "Caller", "phone", 14, 40),
        ("q", "Queue", "queue", 40, 40),
        ("iq", "In-queue", "architect", 66, 22),
        ("ag", "Agent", "agent", 66, 70),
    ], [("c", "q"), ("q", "iq"), ("q", "ag")]),
    "Publish, or the hold is empty",
    [
        ("Caller", "Queue", "Wait", "ACD is already hunting.", "The flow does not choose the agent"),
        ("Flow", "Caller", "Music", "The default action is changeable.", "Menus are not in this flow type"),
        ("Admin", "Flow", "Publish", "Unpublished means unused.", "Republish after edits"),
        ("Email", "Queue", "No default", "Create the email in-queue flow.", "Outbound does not start it"),
        ("Reply", "Flow", "Inbound", "The flow starts on the inbound response.", "Not on the first outbound send"),
    ],
    [
        q("Menus in an in-queue call flow are:", "Not available", ["Required", "The only action", "Limited to 200"], "The overview says menus and reusable tasks are not available."),
        q("The default in-queue call flow handles live calls when:", "You publish it", ["The org is created", "An agent logs in", "A trunk registers"], "It is not automatically published."),
        q("The default action inside that call flow is:", "Music you can change", ["A blind transfer", "An OAuth token", "A WFM forecast"], "The overview describes a single changeable music action."),
        q("An outbound email starts the in-queue email flow immediately?", "No. It starts when an inbound response arrives.", ["Yes", "Only on CX 1", "Only if the name is unique"], "The overview states that launch rule."),
        q("Email in-queue flows differ from calls because:", "There is no built-in default", ["They use RTP", "They cannot be published", "They ignore the queue"], "You create them."),
        q("Editing the music without republishing means:", "The published version is unchanged", ["The Edge reboots", "The division is deleted", "Tokens are refunded"], "Publish is how the runtime hears the edit."),
    ],
    [("Publish", "The default call flow is inert until then."), ("No menus", "In-queue call flows are tasks and states, not menus."), ("Email", "No built-in default. Inbound response launches it."), ("Republish", "Edits do not ride the last publish.")],
    "Publish a hold flow on paper",
    ["Say whether your media has a built-in default.", "If it is voice, say the default action.", "Write the publish step.", "Say when an email in-queue flow starts."],
    "You will not leave a pilot on an unpublished default.",
    ("Pretty flow, old runtime", "The admin added a position announcement. Callers still hear only music.", "Saved: today. Last published: last month.", "The runtime uses the published version.", "Publish the in-queue flow and place a test call before announcing the change."),
    "The in-queue article also describes overall and recurring periods for email and message flows. Re-read those numbers on the page rather than trusting a remembered duration.",
))

add(lesson(
    "a-data", "Data actions and participant data", "Core", 12,
    "A data action calls a system outside the flow. Participant data carries a value to the agent.",
    [
        "Architect’s own description includes data dips and expressions. A Call Data Action is how a flow asks Salesforce, a REST service, or another connector for an answer and then branches. Set Participant Data is how a later agent, script, or screen pop sees what the flow learned. The Salesforce and Zendesk articles both describe screen pop and interaction logging as the agent-facing end of that story.",
        "The action fails closed when the credential is wrong. Salesforce username-password credentials for data actions are on a deprecation path. The migration guide says to use the Salesforce OAuth client-credentials credential: consumer key, consumer secret, and My Domain URL. No change to the request body is required for that credential swap. A flow that worked last year can fail on auth alone.",
    ],
    cites("architect", "sf-oauth", "salesforce", "zendesk"),
    fig("The flow dips out, then writes what it learned onto the conversation.", [
        ("flow", "Flow", "architect", 16, 40),
        ("da", "Data action", "crm", 46, 22),
        ("sf", "Salesforce", "crm", 74, 22),
        ("part", "Participant data", "agent", 46, 72),
    ], [("flow", "da"), ("da", "sf"), ("flow", "part")]),
    "Balance dip, then screen pop",
    [
        ("Flow", "Data action", "Call", "Send an account id.", "Credential is OAuth, not a password"),
        ("Salesforce", "Flow", "Response", "Return a balance or a failure.", "Timeouts need a branch"),
        ("Flow", "Conversation", "Set data", "Store the value for the agent.", "Name it something the screen pop reads"),
        ("Flow", "Queue", "Transfer", "The agent gets the pop with the data.", "The dip is not the queue"),
        ("Admin", "Credential", "Rotate", "Swap username-password for client credentials.", "Request body can stay"),
    ],
    [
        q("Set Participant Data is for:", "Carrying a value to the agent side of the same conversation", ["Choosing the AWS region", "Buying a DID", "Setting fair use"], "It is conversation data, not org configuration."),
        q("The Salesforce data-action credential Genesys tells you to move to is:", "OAuth client credentials with consumer key, secret, and My Domain URL", ["A shared inbox password", "A SIP trunk", "Implicit grant"], "That is the migration guide."),
        q("After that credential swap, the guide says the data-action request body:", "Can stay as it is", ["Must be rewritten in SIP", "Must be deleted", "Must be a WAV file"], "No request or response redesign is required for the swap."),
        q("A data action timeout should:", "Take an explicit failure branch", ["Hang forever", "Delete the queue", "Publish a second org"], "The caller is waiting. Silence is not a design."),
        q("Screen pop for Salesforce is documented as part of:", "Genesys Cloud for Salesforce", ["The Edge firmware", "RFC 3711", "Bullseye ring 6"], "The product article lists screen pop."),
        q("Zendesk’s documented embed also includes:", "Click-to-dial, screen pop, and interaction logs", ["Edge groups", "Number-plan emergency only", "FedRAMP login"], "The Zendesk article lists those agent tools."),
    ],
    [("Data action", "A call out of the flow."), ("Participant data", "What the agent is allowed to see."), ("Salesforce auth", "Client credentials, not username-password."), ("Failure branch", "Required. The caller will not wait politely.")],
    "Write one dip",
    ["Name the external system.", "Name the input.", "Name the participant-data key.", "Write the failure path in one sentence.", "Name the credential type."],
    "The dip has an input, an output, and a failure path.",
    ("Password grant died", "Every Salesforce data action started failing on the same morning.", "Credential type: Salesforce username-password. HTTP 400 from the token URL.", "That credential type is deprecated.", "Create a Connected App and switch the integration to OAuth client credentials. Leave the action contracts alone."),
))

add(lesson(
    "a-common", "Common modules are how you stop copying tasks", "Core", 11,
    "A common module is a flow type you call from other flows. The name is still unique inside that type.",
    [
        "The Architect home page lists common module as its own type so you can build logic once and reuse it across flow types. The 200 character name limit and the per-type uniqueness rule still apply. A module that transfers to a queue hard-codes that queue unless you pass the queue in. Passing the queue in is the difference between a library and a copy.",
        "Reusable tasks inside a single flow are not the same object as a common module shared by many flows. In-queue call flows, notably, do not offer reusable tasks. If the hold experience needs shared logic, you are in a different design conversation than a common module called from an inbound flow.",
    ],
    cites("arch-home", "create-flow", "inqueue"),
    fig("Several flows call one module instead of pasting the task.", [
        ("a", "Sales", "phone", 16, 28),
        ("b", "Service", "phone", 16, 68),
        ("m", "Module", "architect", 55, 46),
        ("q", "Queue", "queue", 84, 46),
    ], [("a", "m"), ("b", "m"), ("m", "q")]),
    "Extract a holiday check",
    [
        ("Admin", "Common module", "Create", "Own name, own type.", "200 character limit"),
        ("Module", "Inputs", "Date and queue", "Do not hide the queue inside the module.", "Callers pass it"),
        ("Inbound", "Module", "Call", "Sales and service both call it.", "One publish updates both"),
        ("In-queue", "Design", "Different tool", "That flow type has no reusable tasks.", "Do not assume the module UI is there"),
    ],
    [
        q("A common module is:", "Its own Architect flow type", ["A queue setting", "A SIP header", "A division you cannot delete"], "The home page lists it beside the other types."),
        q("Two common modules may share a name?", "No. Uniqueness is inside the type.", ["Yes", "Only if unpublished", "Only in satellite regions"], "Per-type uniqueness still applies."),
        q("Hard-coding a queue inside a shared module is risky because:", "Every caller inherits that queue", ["Names can exceed 200 characters automatically", "It deletes Home", "It changes the AWS region"], "Pass the destination in if callers differ."),
        q("In-queue call flows and reusable tasks:", "Reusable tasks are not available in that flow type", ["They are required", "They replace publish", "They set utilization"], "The in-queue overview says so."),
        q("The name limit on the module is:", "200 characters", ["5,000", "30 minutes", "4 chats"], "The create article’s name limit covers flows, including this type."),
        q("A module publish affects:", "Flows that call that module", ["Every trunk in the region", "The fair use price", "Only voicemail"], "Reuse is the point of the type."),
    ],
    [("Type", "Common module is its own tab."), ("Inputs", "Pass the queue. Do not hide it."), ("Uniqueness", "Inside the common-module type."), ("In-queue", "No reusable tasks there.")],
    "Extract one check",
    ["Name the module.", "List its inputs.", "Name two flows that would call it.", "Say why an in-queue flow might not be the caller."],
    "The module has inputs, not hidden queues.",
    ("Copied closed-day prompt", "Four flows still say yesterday’s holiday hours.", "Logic pasted into each flow. No common module.", "There is no single publish.", "Move the date check into a common module and call it."),
))

add(lesson(
    "a-secure", "Secure call flows keep digits away from the recording", "Core", 12,
    "A secure flow is how a caller enters a card number without that audio being recorded or shown to the agent.",
    [
        "The Architect home page describes secure call flows as the way to stop system recording and agent access while a caller enters sensitive digits, such as a payment. The create article says these flows are either agent-initiated or started by another call flow, and that Genesys uses a blind transfer rather than a consultation VXML transfer so the transfer does not fail.",
        "This is not the same control as a queue recording policy. Recording policies decide which ACD calls are recorded at all. A secure flow is a hole in that recording for a segment. You still design the return path to the agent, and you still do not log the digits into participant data “for the screen pop.” That would undo the point.",
    ],
    cites("arch-home", "create-flow", "recording"),
    fig("The secure segment is a blind transfer away from the recorded agent leg.", [
        ("ag", "Agent", "agent", 14, 40),
        ("sec", "Secure flow", "architect", 48, 40),
        ("pay", "Payment", "phone", 78, 22),
        ("rec", "Recording", "wem", 78, 72),
    ], [("ag", "sec"), ("sec", "pay")]),
    "Take a payment without leaking it",
    [
        ("Agent", "Flow", "Start secure", "The flow can be agent-initiated.", "Or another flow can call it"),
        ("Platform", "Agent", "Blind transfer", "Not a consultation VXML transfer.", "Documented to avoid failure"),
        ("Caller", "Flow", "Digits", "Collect the payment input.", "Do not copy it to participant data"),
        ("Flow", "Agent", "Return", "The agent resumes without the digits.", "Recording resumes under policy"),
        ("Policy", "Call", "Separate", "The queue policy still decides the rest of the call.", "Secure is a segment"),
    ],
    [
        q("A secure call flow exists to:", "Block recording and agent access during sensitive input", ["Speed up bullseye", "Replace BYOC", "Store the card in participant data"], "The home page states the purpose."),
        q("The transfer type the create article specifies is:", "Blind, not consultation VXML", ["Consultation only", "REFER with no answer", "An email transfer"], "Blind is the documented choice."),
        q("Who can start a secure flow?", "An agent or another call flow", ["Only a satellite region", "Only WFM", "Only a trunk"], "The create article lists both initiators."),
        q("Putting the card number in participant data is:", "A way to undo the secure flow", ["Required", "How screen pop is documented", "How DCVP works"], "The agent and the logs would see the value."),
        q("Queue recording policy and a secure flow:", "Answer different questions. Policy selects calls. The secure flow punches a hole in a segment.", ["Are the same setting", "Both live on the trunk only", "Both are fair-use meters"], "About recording describes policies. Architect describes the secure flow."),
        q("After the secure segment the design still needs:", "A return to the agent", ["A new organization", "A deleted Home division", "An unpublished in-queue flow"], "The caller and the agent still have a conversation to finish."),
    ],
    [("Purpose", "Hide a sensitive entry from recording and from the agent."), ("Blind", "Not a consultation VXML transfer."), ("Do not log", "Participant data would leak the digits."), ("Policy", "Still decides whether the rest of the call is recorded.")],
    "Trace a payment",
    ["Say who starts the flow.", "Say why the transfer is blind.", "Say where the digits must not be written.", "Say how the agent gets the caller back."],
    "The payment path has a return and no copy of the digits.",
    ("Digits in the note", "QA finds card numbers in agent notes.", "Secure flow used. A later Set Participant Data stored the collected input. The script wrote it into the note.", "The secure segment never reached the recording, and the flow published it anyway.", "Stop writing the collected input to participant data or notes. Confirm the secure flow is the only collector."),
))

add(lesson(
    "a-botcall", "Call a bot from the inbound flow", "Core", 13,
    "Dialog Engine bot flows and digital bot flows are Architect flow types. The inbound flow calls them. It does not become them.",
    [
        "Genesys documents Dialog Engine Bot Flows for voice and digital flows, and Digital Bot Flows for message experiences. The inbound article shows creating a bot, asking a question, and calling that bot from the inbound flow. Intents come back as outcomes the flow can branch on. A banking template in that article checks a balance or finds a branch.",
        "Call Bot Flow and Call Digital Bot Flow are different actions for different bot types. An external bot connector is a third action family. The connector list changes. Confirm the current connector in Architect rather than designing around a vendor this lab does not have an open product page for. Always give the bot a failure output that transfers to a queue.",
    ],
    cites("dialog", "digital-bot", "bot-inbound", "architect"),
    fig("The inbound flow calls a bot and still owns the failure path.", [
        ("in", "Inbound", "phone", 14, 40),
        ("bot", "Bot flow", "bot", 46, 22),
        ("ok", "Intent", "architect", 74, 22),
        ("q", "Queue", "queue", 74, 70),
    ], [("in", "bot"), ("bot", "ok"), ("bot", "q")]),
    "Ask, then fall back to a human",
    [
        ("Admin", "Bot flow", "Create", "Pick Dialog Engine or digital.", "They are different types"),
        ("Bot", "Caller", "Question", "Voice plays it. Chat shows it.", "The article’s banking example"),
        ("Inbound", "Bot", "Call Bot Flow", "Bind the outputs.", "Intent is data"),
        ("Bot", "Inbound", "Failure", "No match, timeout, or error.", "Transfer to ACD"),
        ("Admin", "Insights", "Read", "Flow Insights shows what actually ran.", "Publish first"),
    ],
    [
        q("Dialog Engine Bot Flows and Digital Bot Flows are:", "Both Architect bot types with different call actions", ["The same flow", "SIP trunks", "Divisions"], "The product documents them as related and distinct."),
        q("The banking example lets the caller:", "Check a balance or find a branch", ["Buy BYOC", "Set a concurrent peak", "Delete a recording policy"], "That is the documented template."),
        q("A bot with no failure path:", "Strands the caller when the bot misses", ["Is required by RFC 3261", "Publishes the queue", "Sets utilization to 4"], "Transfer to ACD belongs on the failure output."),
        q("Flow Insights is for:", "Seeing how often flow pieces actually run", ["Buying numbers", "Editing fair use", "Orbiting the 3D map"], "The Architect bot material points at Flow Insights."),
        q("An external bot vendor should be chosen from:", "The connectors currently shown in Architect", ["This lab’s memory of 2023", "A forum dump", "The Edge serial number"], "Connector lists change. Confirm them in the product."),
        q("Voice versus chat for the same question action:", "Voice speaks the question. Chat displays it.", ["Both send RTP", "Both require a trunk", "Chat uses 911"], "The bot article describes that split."),
    ],
    [("Two bot types", "Dialog Engine and digital."), ("Call action", "Match the action to the type."), ("Failure", "Always a queue."), ("Insights", "After publish, read what ran.")],
    "Wire a bot with a fallback",
    ["Name the bot type.", "Write the question.", "Name two intents.", "Name the queue on failure.", "Say where you would read Flow Insights."],
    "The picture shows a bot and a queue, not a bot instead of a queue.",
    ("Bot dead end", "After hours, callers who ask for an agent hear the bot ask the same question again.", "Call Bot Flow failure output: empty.", "There is no transfer.", "Connect the failure output to the support queue and publish."),
))

add(lesson(
    "a-publish", "Publish, division, and Flow Insights", "Core", 12,
    "A saved flow is a draft. The runtime uses the published version. Insights tell you whether anyone hit it.",
    [
        "Create, edit, and publish are different moments. In-queue flows make that obvious because the default exists and still does nothing until publish. The same discipline applies to inbound flows, bots, and common modules. Flow Insights, referenced from the bot documentation, shows how often pieces of a flow run. A flow that Insights says never runs is usually a routing problem: the call route, the queue’s in-queue selection, or the bot call is pointing somewhere else.",
        "The flow’s division controls who can edit it. An admin in the wrong division will swear the flow is missing. It is not missing. Their role is not granted on that division. Fix the grant or move the flow. Do not create a second copy under a new name and leave the published one in place.",
    ],
    cites("create-flow", "inqueue", "dialog", "divisions"),
    fig("Draft, published runtime, and the route that points at it.", [
        ("draft", "Draft", "architect", 16, 40),
        ("pub", "Published", "architect", 42, 40),
        ("route", "Call route", "trunk", 68, 22),
        ("ins", "Insights", "wem", 68, 70),
    ], [("draft", "pub"), ("pub", "route"), ("pub", "ins")]),
    "Ship a change without leaving the old runtime up",
    [
        ("Author", "Draft", "Save", "The editor has the new prompt.", "Callers do not"),
        ("Author", "Publish", "Runtime", "Now the edge that executes flows can see it.", "Republish after every fix"),
        ("Admin", "Call route", "Point", "A DID still runs whichever flow the route names.", "Publishing is not attaching"),
        ("Analyst", "Insights", "Read", "Zero runs means the route or the call action is elsewhere.", "Not a codec problem"),
        ("Admin", "Division", "Grant", "Editors need the flow’s division.", "A copy hides the real flow"),
    ],
    [
        q("Saving a flow updates callers when:", "You also publish, and the route or queue actually uses that flow", ["You save", "You refresh the browser", "You change theme"], "Publish plus a reference is the runtime."),
        q("Flow Insights showing zero executions usually means:", "Nothing is invoking that published flow", ["RTP is one-way", "The 30 minute concurrent rule", "The name is 200 characters"], "Look at the call route, the queue setting, or the Call Bot Flow action."),
        q("An admin who cannot see a flow should check:", "The flow’s division and their role grant", ["The SIP codec first", "The satellite region first", "The wrap-up code first"], "Divisions hide objects from roles that are not granted."),
        q("Creating a second copy instead of granting access:", "Leaves the published original in place and splits the design", ["Is the documented fix", "Deletes the original", "Moves the AWS region"], "Fix the grant or move the flow."),
        q("The default in-queue flow is the teaching example of:", "Exists, saved, and still unused until publish", ["A flow that cannot be published", "A trunk", "A token"], "That is the in-queue article’s warning."),
        q("Call-route attachment and publish are:", "Both required. Publish makes a version. The route selects it.", ["The same click", "Illegal together", "Only for bots"], "A published flow nobody references does not answer the DID."),
    ],
    [("Save", "Draft."), ("Publish", "Runtime version."), ("Route", "What actually invokes it."), ("Division", "Who is allowed to see it.")],
    "Ship a one-line prompt change",
    ["Edit the prompt.", "Publish.", "Name the call route or queue that must reference it.", "Say what zero Flow Insights executions would mean."],
    "The change has a publish and a reference, not only a save.",
    ("Two billing flows", "Half the DIDs still play the old hours.", "Billing inbound published today. Call route for +15555550199 still names Billing inbound legacy.", "Publish did not move the route.", "Point the route at the new flow, place a test call, then retire the legacy flow."),
))
