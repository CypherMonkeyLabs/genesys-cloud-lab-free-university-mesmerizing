from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "ai",
    "title": "Genesys AI and bots",
    "kicker": "Beside the agent",
    "accent": 3,
    "summary": "Dialog Engine and digital bots, failure paths, Agent Copilot, tokens, and the AI exams as the catalog names them.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "g-kinds", "Two Architect bot types, plus Copilot beside the agent", "Core", 12,
    "A bot flow talks to the customer. Agent Copilot talks to the agent. They are different products on different pages.",
    [
        "Architect documents Genesys Dialog Engine Bot Flows and Genesys Digital Bot Flows as flow types. An inbound flow calls them with the matching action. Agent Copilot, on its own overview, works inside the agent experience: knowledge, transcripts, scripts, next best action, and notes. Copilot is part of the CX 4 story on the package overview, along with Journey Management and a published token allotment.",
        "Do not design a “bot” and assume it covers both. A voice bot that cannot reach a queue is a trapped caller. A Copilot summary that Virtual Supervisor reuses is a billing note on the STA FAQ, not a second bot.",
    ],
    cites("dialog", "digital-bot", "copilot", "overview"),
    fig("Bots face the customer. Copilot faces the agent.", [
        ("cust", "Customer", "phone", 12, 40),
        ("bot", "Bot flow", "bot", 40, 22),
        ("ag", "Agent", "agent", 68, 40),
        ("cp", "Copilot", "wem", 90, 22),
    ], [("cust", "bot"), ("bot", "ag"), ("ag", "cp")]),
    "Name which AI the design actually needs",
    [
        ("Caller", "Self-serve", "A bot flow", "Dialog Engine or digital.", "Plus a failure queue"),
        ("Agent", "Help during the call", "Agent Copilot", "Knowledge, transcript, scripts, notes.", "CX 4 on the overview"),
        ("QA", "Score later", "STA and QM", "Not a bot.", "Tokens, per the FAQ"),
        ("Buyer", "Journey", "Named on CX 4", "Separate from the bot flow type.", "Read the overview"),
    ],
    [
        q("Dialog Engine Bot Flows and Digital Bot Flows are:", "Architect flow types", ["SIP trunk types", "Edge models", "Fair-use meters"], "The Architect articles define them."),
        q("Agent Copilot is aimed at:", "The agent during the interaction", ["The carrier SBC", "The PSAP", "The number plan"], "The Copilot overview describes the agent experience."),
        q("CX 4 on the package overview adds:", "Agent Copilot, Journey Management, and AI tokens", ["A second core region", "Unlimited trunks", "UCCE scripting"], "That is the overview’s list."),
        q("A bot and Copilot in one sentence without a failure queue:", "Still needs a human path for the caller", ["Is complete", "Replaces ACD", "Sets ACW"], "The bot articles expect a way out."),
        q("Virtual Supervisor reusing a Copilot summary is documented as:", "Not a second summary bill, on the STA FAQ", ["A new trunk", "A division move", "An implicit grant"], "Re-read the FAQ before you model cost."),
        q("Journey Management is:", "Named with CX 4, and not the same object as a bot flow", ["A queue", "A phone trunk", "An RFC"], "Do not collapse the overview into one feature."),
    ],
    [("Bot", "Faces the customer."), ("Copilot", "Faces the agent."), ("CX 4", "Where the overview places Copilot."), ("QA", "STA plus a form, not a bot.")],
    "Split the design",
    ["What the caller should do alone.", "What the agent should see.", "The package.", "The queue if the bot fails."],
    "Four different answers, not one “AI” line.",
    ("One SKU story", "The statement of work says “AI” and nobody knows whether a bot, Copilot, or scoring was sold.", "CX 2 purchased. Copilot pages absent.", "The package does not include the CX 4 row.", "Rewrite the scope to the package, or change the package."),
))

add(lesson(
    "g-dialog", "Dialog Engine bot flows are voice and digital intents", "Core", 12,
    "You build the bot in Architect, then the inbound flow calls it.",
    [
        "The Dialog Engine article and the inbound-bot article show a bot that asks a question and returns an intent the flow can branch on. The banking example checks a balance or finds a branch. Voice speaks the question. Chat displays it. Intents are outcomes, not a hidden script the ACD can guess.",
        "Call Bot Flow is the action for this bot type. A digital-only bot uses a different action, covered next. Give every no-match, timeout, and error output a queue. Flow Insights, after you publish, shows whether anyone reached the bot.",
    ],
    cites("dialog", "bot-inbound", "architect"),
    fig("Ask, return an intent, or leave to a queue.", [
        ("in", "Inbound", "phone", 14, 40),
        ("bot", "Dialog bot", "bot", 46, 22),
        ("ok", "Intent", "architect", 78, 22),
        ("q", "Queue", "queue", 78, 68),
    ], [("in", "bot"), ("bot", "ok"), ("bot", "q")]),
    "Build the banking shape",
    [
        ("Admin", "Bot", "Create a Dialog Engine bot flow", "Name it like a flow.", "Unique per type, 200 characters"),
        ("Bot", "Question", "Balance or branch", "The documented example.", "Your domain will differ"),
        ("Inbound", "Action", "Call Bot Flow", "Bind outputs.", "Not the digital action"),
        ("Fail", "Queue", "Transfer to ACD", "No match and errors.", "Publish, then read Insights"),
    ],
    [
        q("The banking template in the inbound bot article:", "Checks a balance or finds a branch", ["Buys a trunk", "Sets a concurrent peak", "Deletes a division"], "Use it as a shape, not as your business."),
        q("Voice and chat for the same question:", "Voice speaks it. Chat displays it.", ["Both use RTP", "Both use 911", "Both require an Edge"], "The article describes that split."),
        q("The action that calls a Dialog Engine bot is:", "Call Bot Flow", ["Call Digital Bot Flow", "Transfer to ACD only", "Disconnect"], "Match the action to the type."),
        q("An intent is:", "An outcome the inbound flow can branch on", ["A skill proficiency", "A fair-use meter", "A login host"], "Bind it to a path."),
        q("Flow Insights is useful after:", "You publish and traffic runs", ["You save a draft", "You create an OAuth secret", "You move regions"], "A draft has no runtime to measure."),
        q("No-match with an empty failure output:", "Strands the caller", ["Routes by bullseye automatically", "Sends a SIP 200", "Opens Copilot"], "Transfer to ACD belongs there."),
    ],
    [("Example", "Balance or branch."), ("Action", "Call Bot Flow."), ("Intent", "A branch in the inbound flow."), ("Failure", "A queue.")],
    "Sketch three outputs",
    ["The question.", "Two intents.", "The failure queue.", "Where you will read Flow Insights."],
    "Every output has a next action.",
    ("Wrong action", "The inbound flow cannot see the bot’s intents.", "Action used: Call Digital Bot Flow. Bot type: Dialog Engine.", "The action and the type disagree.", "Use Call Bot Flow and republish."),
))

add(lesson(
    "g-digital", "Digital bot flows are a different call", "Core", 11,
    "Message experiences use Digital Bot Flows and Call Digital Bot Flow.",
    [
        "The digital bot article describes Genesys Digital Bot Flows for message experiences. They are Architect flows, and they are not the Dialog Engine type with a renamed action. An inbound message flow calls them with Call Digital Bot Flow. Mixing the actions is a publish-time or runtime miss, not a wording preference.",
        "Digital bots still need a human path. The message queue, the in-queue message flow, and the error-event queue from the Architect create-flow rules still apply. A bot that handles the first turn does not delete those requirements.",
    ],
    cites("digital-bot", "bot-inbound", "create-flow"),
    fig("A message flow calls a digital bot, and still has a queue.", [
        ("msg", "Message", "phone", 16, 40),
        ("db", "Digital bot", "bot", 48, 40),
        ("q", "Queue", "queue", 80, 40),
    ], [("msg", "db"), ("db", "q")]),
    "Keep the digital path honest",
    [
        ("Admin", "Type", "Digital Bot Flow", "Not Dialog Engine.", "The article separates them"),
        ("Flow", "Action", "Call Digital Bot Flow", "On the inbound message flow.", "Match the type"),
        ("Admin", "Error queue", "Still required", "Message flows need an error-event queue.", "Create-flow article"),
        ("Fail", "Human", "Transfer", "When the bot cannot finish.", "In-queue message behavior still exists"),
    ],
    [
        q("Digital Bot Flows are for:", "Message experiences", ["Emergency calling", "Edge groups", "Concurrent billing"], "That is the article’s scope."),
        q("The matching action is:", "Call Digital Bot Flow", ["Call Bot Flow", "Play Audio only", "Set utilization"], "Do not reuse the voice action."),
        q("An inbound message flow still needs:", "An error-event queue", ["A premises Edge", "A 988 plan", "A predictive model"], "The create-flow article requires it."),
        q("A digital bot replaces the queue when:", "It does not. Keep a human path.", ["Always", "On CX 1", "If the name is unique"], "Bots miss."),
        q("Using Call Bot Flow on a digital bot is:", "A type mismatch", ["Best practice", "Required for chat", "A region setting"], "Match action to type."),
        q("In-queue message flows:", "Still matter after the bot hands off", ["Are deleted by bots", "Are phone trunks", "Are tokens"], "Read the in-queue rules for messages."),
    ],
    [("Type", "Digital Bot Flow."), ("Action", "Call Digital Bot Flow."), ("Error queue", "Still required."), ("Human", "Still required.")],
    "Check a message design",
    ["Bot type.", "Call action.", "Error-event queue.", "Handoff queue."],
    "All four names are written down.",
    ("Voice action on chat", "The message flow errors when it hits the bot.", "Call Bot Flow pointed at a Digital Bot Flow.", "Wrong action.", "Swap the action and publish."),
))

add(lesson(
    "g-fail", "Every bot has a failure output to a queue", "Core", 11,
    "No-match, timeout, and error are normal. The queue is the design.",
    [
        "The inbound bot article’s useful pattern is a question, an intent, and a way out. Treat failure as a path you draw, not as an exception. After hours, the way out may be a different queue or a callback, still inside Architect, still published.",
        "External bot connectors exist as a separate action family. The list changes. This lab will not name a vendor. Confirm the connector in Architect, and still draw the failure output. A connector timeout is the same caller problem as a no-match.",
    ],
    cites("bot-inbound", "dialog", "architect"),
    fig("Three bad outcomes, one queue.", [
        ("nm", "No match", "bot", 18, 22),
        ("to", "Timeout", "bot", 48, 22),
        ("er", "Error", "bot", 78, 22),
        ("q", "Queue", "queue", 48, 70),
    ], [("nm", "q"), ("to", "q"), ("er", "q")]),
    "Draw the three exits",
    [
        ("No match", "Queue", "Transfer to ACD", "The caller asked for a person or said something new.", "Do not re-ask forever"),
        ("Timeout", "Queue", "Same or a shorter path", "Silence is not consent.", "Mind the in-queue experience"),
        ("Error", "Queue", "Connector or action failure", "Including an external bot.", "Log it in Flow Insights"),
        ("Hours", "Schedule", "A second queue or callback", "Still published.", "Do not leave the output empty at night"),
    ],
    [
        q("No-match should:", "Transfer to a queue or another published path", ["Loop the question", "Disconnect with no message", "Change regions"], "The caller needs a way out."),
        q("An external bot connector:", "Still needs a failure output", ["Cannot fail", "Replaces the inbound flow", "Is chosen from memory"], "Confirm the connector in Architect."),
        q("This lab names external bot vendors:", "It does not", ["It must", "Only Cisco", "Only on CX 1"], "The list changes."),
        q("After-hours failure outputs:", "Are part of the design, not a later project", ["Are illegal", "Use 911", "Disable recording"], "Draw them."),
        q("Flow Insights after a week of errors tells you:", "Which output is actually firing", ["The fair-use price", "The login host", "The exam code"], "Publish first."),
        q("Re-asking the same question forever is:", "A trapped caller", ["Bullseye", "Preferred agent routing", "A secure flow"], "Cap the retries and transfer."),
    ],
    [("No match", "A path."), ("Timeout", "A path."), ("Error", "A path."), ("Vendor", "Confirm in product. Still draw the exit.")],
    "Trace a timeout",
    ["What the caller hears.", "Which queue answers.", "What Insights will show.", "What happens after hours."],
    "None of the four is “empty”.",
    ("Retry loop", "Callers who say “agent” hear the menu until they hang up.", "No-match output connected to the same Ask.", "There is no exit.", "Connect no-match to the support queue."),
))

add(lesson(
    "g-copilot", "Agent Copilot assists the person who stayed on the interaction", "Core", 12,
    "Knowledge, transcripts, scripts, next best action, and notes. The benefit is described as surviving a blind transfer.",
    [
        "The Agent Copilot overview lists knowledge articles, transcripts, custom scripts, next best action, and forms and notes: reason, resolution, and a possible wrap-up. It is help for the agent, grounded in content you maintain. A knowledge article that is wrong will be repeated confidently. Curate the source.",
        "The overview says the benefits survive a blind transfer, so the next agent is not starting from an empty panel. That is not a reason to blind-transfer a payment. Secure flows still exist to keep digits out of recordings and out of participant data. Copilot does not collect card numbers.",
    ],
    cites("copilot", "create-flow", "overview"),
    fig("Copilot reads curated knowledge and stays with the conversation.", [
        ("kn", "Knowledge", "wem", 16, 28),
        ("cp", "Copilot", "bot", 46, 40),
        ("ag", "Agent", "agent", 78, 28),
        ("nx", "Next agent", "agent", 78, 68),
    ], [("kn", "cp"), ("cp", "ag"), ("ag", "nx")]),
    "Turn Copilot on without lying to the agent",
    [
        ("Content", "Articles", "Only maintained knowledge", "Wrong articles get repeated.", "Name an owner"),
        ("Agent", "Panel", "Transcript and scripts", "The overview lists them.", "Plus next best action"),
        ("Notes", "Wrap-up help", "Reason and resolution", "A possible wrap-up, not a forced code.", "The agent still owns the code"),
        ("Transfer", "Blind", "Context can remain", "The overview’s claim.", "Secure flows still hide digits"),
    ],
    [
        q("Agent Copilot’s overview includes:", "Knowledge, transcripts, scripts, next best action, and notes", ["SIP trunks", "Edge groups", "Number plans"], "That is the agent-facing list."),
        q("A stale knowledge article will:", "Be repeated to the agent as if it were current", ["Fix itself", "Disable ACD", "Move the region"], "Curate the source."),
        q("Notes described on the overview include:", "Reason, resolution, and a possible wrap-up", ["The carrier ACL", "The OAuth secret", "The PSAP"], "The agent still confirms the wrap-up code."),
        q("Benefits surviving a blind transfer means:", "The next agent can still see the assistance", ["Card numbers are stored", "The queue is deleted", "Recording is disabled"], "It is not a PCI design."),
        q("Secure flows remain necessary because:", "Payment digits must stay out of recordings and participant data", ["Copilot replaces them", "They set bullseye", "They buy tokens"], "Copilot is not a secure flow."),
        q("Copilot is packaged on the overview as:", "A CX 4 addition", ["A CX 1 voice feature", "An Edge firmware", "A default number plan"], "Read the package stack."),
    ],
    [("Sources", "Knowledge you maintain."), ("Panel", "Transcript, script, next action."), ("Notes", "Reason, resolution, possible wrap-up."), ("Transfer", "Help can remain. Digits still must not.")],
    "Name the sources",
    ["Who owns the knowledge articles.", "Which script Copilot may use.", "What the note should contain.", "Which flow still hides payment digits."],
    "An owner is a person, not “the AI”.",
    ("Stale article", "Agents quote a retired discount because Copilot surfaced it.", "Knowledge article last reviewed two years ago.", "The source was wrong.", "Unpublish the article and name a reviewer."),
))

add(lesson(
    "g-tokens", "Tokens are a published allotment, and a FAQ ratio you re-read", "Advanced", 12,
    "The overview publishes CX 4 token counts. The STA FAQ publishes how AI scoring spends them.",
    [
        "The package overview lists 30 AI tokens for a named CX 4 user and 39 for a concurrent user. That sentence is the allotment story. The STA FAQ says AI scoring needs STA, quality management, and AI Experience Tokens, and that one token covers 20 AI-scored evaluations. It also says a Copilot summary reused by Virtual Supervisor is not billed twice. Re-read both pages before you put a number in a contract.",
        "Bots are not the same meter. Do not assume a Dialog Engine flow spends the scoring token. If a page does not say it, this lab will not say it. Fair use is a third page, for pooled allowances such as API requests and transcription, and it is not the token table.",
    ],
    cites("overview", "sta-faq", "fair", "copilot"),
    fig("Allotment on the overview. Consumption on the FAQ.", [
        ("ov", "Overview", "region", 18, 40),
        ("faq", "STA FAQ", "wem", 50, 40),
        ("sc", "AI score", "bot", 82, 40),
    ], [("ov", "faq"), ("faq", "sc")]),
    "Budget from the pages, not from this paragraph",
    [
        ("Buyer", "Allotment", "30 named, 39 concurrent", "Overview, CX 4.", "Confirm the live sentence"),
        ("QA", "Scoring", "STA, QM, tokens", "FAQ prerequisites.", "Ratio: re-read"),
        ("QA", "Summary reuse", "Not double-billed", "Copilot summary in Virtual Supervisor.", "FAQ"),
        ("Architect", "Bot", "Do not invent a token price", "Unless a page states it.", "Fair use is a different meter"),
    ],
    [
        q("The overview’s named CX 4 token allotment is:", "30", ["39", "20", "1"], "39 is the concurrent figure."),
        q("The concurrent allotment on that overview is:", "39", ["30", "100", "5"], "Do not swap the two."),
        q("AI scoring consumes tokens only when:", "STA, QM, and AI Experience Tokens are all in place", ["A queue exists", "An Edge exists", "GC-GCP is passed"], "The FAQ lists three gates."),
        q("The FAQ’s evaluations-per-token note should be:", "Re-read before you budget", ["Memorized forever", "Ignored", "Copied into a trunk"], "The page can change."),
        q("A Copilot summary shown again by Virtual Supervisor:", "Is not a second summary bill, per the FAQ", ["Always doubles", "Deletes STA", "Disables the bot"], "That is the FAQ’s billing note."),
        q("Fair use and AI tokens are:", "Different pages. Do not merge them.", ["The same table", "Both RFC 3261", "Both Edge settings"], "Transcription minutes and API calls have their own fair-use rows."),
    ],
    [("30", "Named allotment on the overview."), ("39", "Concurrent allotment."), ("20", "FAQ’s evaluations per scoring token. Re-read."), ("Bots", "No invented token price.")],
    "Write the budget footnote",
    ["The overview sentence.", "The FAQ ratio sentence, dated by you when you read it.", "What you will not claim about bot pricing.", "Who re-reads both before renewal."],
    "The footnote names pages, not a guess.",
    ("Invented bot price", "A proposal says each bot intent costs one AI token.", "No article in the design packet states that.", "The number was invented.", "Delete it. Cite the overview and the FAQ only for what they say."),
    "Token ratios and allotments change. The numbers in this lesson match the pages as read for this lab on 14 October 2026. Re-open them.",
))

add(lesson(
    "g-cert", "The AI exams are named on the catalog, one exam each", "Core", 10,
    "Two AI certifications. No invented exam codes.",
    [
        "The Genesys Cloud exams page lists AI certifications separately from the Professional and Developer certifications and from the specialist exams. As read on 14 October 2026, each of AI – GPE & GPR and Digital Bots & Knowledge is one exam. The catalog links them to course 17671 and course 18174. This lab does not invent a GCX- prefix for either.",
        "Speech and Text Analytics is a specialist certification on the same catalog, not one of those two AI exams. Passing a bot course does not pass the STA specialist exam. The announcement page covers webcam and practice-exam notes. Read it before you book.",
    ],
    cites("certs", "cert-note"),
    fig("Two AI exams, plus a separate STA specialist.", [
        ("gpe", "GPE and GPR", "bot", 16, 40),
        ("dig", "Digital bots", "bot", 50, 40),
        ("sta", "STA specialist", "wem", 84, 40),
    ], [("gpe", "dig"), ("dig", "sta")]),
    "Pick the exam that matches the work",
    [
        ("Work", "Predictions and routing AI", "AI – GPE & GPR", "Catalog course 17671.", "One exam"),
        ("Work", "Bots and knowledge", "Digital Bots & Knowledge", "Catalog course 18174.", "One exam"),
        ("Work", "Topics and transcription", "STA specialist", "A different row.", "Do not swap them"),
        ("Book", "Announcement", "Webcam and practice exams", "Read the current note.", "No voucher story invented here"),
    ],
    [
        q("AI – GPE & GPR on the catalog is:", "One exam, linked from course 17671", ["A specialist with a GCX code this lab invented", "The same as GC-GCP", "An Edge exam"], "Use the catalog name."),
        q("Digital Bots & Knowledge is:", "A separate one-exam AI certification, course 18174", ["Included automatically with GPE", "The STA specialist", "A Cisco exam"], "Do not merge the rows."),
        q("The STA specialist exam is:", "Its own catalog row", ["The same as Digital Bots", "Retired in this lab’s notes", "GC-GCD"], "Topics and bots are different jobs."),
        q("This lab assigns GCX- codes to AI exams:", "It does not. Older community posts are not the catalog.", ["It must", "Only for bots", "Only for STA"], "The catalog is the source."),
        q("Before you book, also read:", "The technical certifications announcement", ["A dump site", "RFC 5737", "The BYOC quick start"], "Webcam and practice-exam notes live there."),
        q("Passing a digital bot course means:", "You prepared for that exam, not for every other row", ["You are GC-GCP", "You can skip STA", "You own CX 4"], "Each exam is separate."),
    ],
    [("GPE & GPR", "Course 17671. One exam."), ("Digital bots", "Course 18174. One exam."), ("STA", "A specialist row."), ("Codes", "No invented GCX- prefix.")],
    "Match three jobs to three rows",
    ["A predictive-routing specialist.", "A bot builder.", "A speech-analytics admin.", "The page you will re-open before paying."],
    "Three different catalog rows.",
    ("Wrong row", "A bot builder studies the professional implementation course and is surprised by intent questions.", "They booked GC-GCP.", "The work matched Digital Bots & Knowledge.", "Rebook using the catalog row."),
    "Course numbers were taken from the Genesys Cloud exams catalog as read on 14 October 2026. Confirm before you enroll.",
))
