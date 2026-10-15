from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "sta",
    "title": "Speech and text analytics",
    "kicker": "Listen after",
    "accent": 4,
    "summary": "What gets transcribed, how sentiment and topics are used, and why analysis is not the same thing as the live conversation.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "s-scope", "STA reads the conversation after the channel has it", "Core", 12,
    "Speech and text analytics covers voice and digital interactions. It is not a second ACD.",
    [
        "The overview and the about page describe transcription and analysis of voice interactions and of digital interactions such as email, message, and chat. Voice coverage described there includes the IVR, voice bots, the ACD portion, the agent, conferences, and voicemail. Digital coverage follows the text the customer and the agent already exchanged.",
        "STA is a CX 3-and-above story in the current package overview, because that is where transcription minutes are named. Quality management can exist without it. AI scoring cannot. Do not promise a dialect list or a price from memory. Those tables live on the current pages and they move.",
    ],
    cites("sta", "sta-about", "sta-faq", "overview"),
    fig("Voice and digital both become text the analytics layer can search.", [
        ("ivr", "IVR", "architect", 12, 28),
        ("acd", "ACD", "queue", 36, 28),
        ("dig", "Digital", "phone", 60, 28),
        ("sta", "STA", "bot", 84, 55),
    ], [("ivr", "sta"), ("acd", "sta"), ("dig", "sta")]),
    "Name what will be transcribed",
    [
        ("Voice", "IVR and bots", "In scope when the page says so", "The caller’s menu path is speech too.", "Not only the agent"),
        ("Voice", "ACD and conference", "The human portion", "Including more than one party when the article includes conferences.", "Voicemail is called out separately"),
        ("Digital", "Email, message, chat", "Already text", "Analysis does not wait for a codec.", "Still needs the feature"),
        ("Buyer", "Package", "CX 3 for transcription minutes", "The overview is the package source.", "QM alone is not STA"),
    ],
    [
        q("Voice transcription described on the STA pages includes:", "IVR, voice bots, ACD, agents, conferences, and voicemail", ["Only the agent greeting", "Only SIP OPTIONS", "Only 911"], "The overview’s scope is wider than the agent leg."),
        q("Digital analysis covers:", "Email, message, and chat text", ["RTP ports", "Edge serial numbers", "Login hosts"], "Those channels are already text."),
        q("Transcription minutes are introduced on the package overview at:", "Genesys Cloud CX 3", ["CX 1", "A free AppFoundry trial", "The Edge"], "CX 3 is where the overview names them."),
        q("A dialect or price you remember from a slide is:", "Not a source. Re-open the STA pages.", ["Permanent", "An RFC", "A queue name"], "This lab does not copy those tables."),
        q("STA and quality management are:", "Related, and not the same product row", ["The same switch", "Both SIP", "Both number plans"], "QM can exist where transcription does not."),
        q("Voicemail is:", "Called out in the voice scope, not ignored", ["Never transcribed", "A trunk type", "A division"], "Include it when you scope a program."),
    ],
    [("Voice scope", "IVR through voicemail, as the page lists it."), ("Digital", "Email, message, chat."), ("Package", "Transcription minutes at CX 3."), ("Tables", "Re-read dialects and prices.")],
    "Write the scope sentence",
    ["List the voice legs you will transcribe.", "List the digital channels.", "Name the package that includes transcription minutes.", "Write “dialects and prices: see the live page.”"],
    "The sentence matches the overview, not a slide.",
    ("Agent-only transcript", "Topics never fire on the IVR, and nobody knows why.", "Program: agent leg only. IVR prompts contain the phrase you wanted.", "The scope was narrower than the page.", "Include the IVR leg if the phrase is spoken there, and re-check the overview."),
    "Confirm dialect coverage and any per-minute price on the current STA pages. This lesson does not list them.",
))

add(lesson(
    "s-sentiment", "Sentiment is a label on the text, not a mood you can argue with", "Core", 11,
    "Sentiment scores the customer’s language. Use it as a filter, then listen.",
    [
        "The STA pages describe sentiment so you can find interactions that went badly or well without listening to all of them. A negative label is a queue for a human, not a fact about the customer’s life. Sarcasm, a product name that sounds negative, and a language the model handles poorly will all fool a score.",
        "Quality forms and coaching still need the recording or the transcript. Sentiment does not replace the form from the quality track. The FAQ is also where AI scoring’s prerequisites are written. Sentiment by itself does not spend that story.",
    ],
    cites("sta", "sta-about", "sta-faq", "qm"),
    fig("Sentiment filters the pile. A person still listens.", [
        ("txt", "Transcript", "bot", 18, 40),
        ("sent", "Sentiment", "wem", 48, 40),
        ("ear", "Evaluator", "agent", 80, 40),
    ], [("txt", "sent"), ("sent", "ear")]),
    "Use sentiment as a filter",
    [
        ("Admin", "Program", "Turn sentiment on for the queue", "Only where you will act on it.", "A score nobody reads is noise"),
        ("Sup", "Filter", "Negative customer language", "Open the transcript.", "Do not coach from the label alone"),
        ("QA", "Form", "Still the rubric", "Sentiment is not a question weight.", "QM owns the score"),
        ("Review", "False hits", "Product names and sarcasm", "Note them.", "Tune phrases, do not blame the agent"),
    ],
    [
        q("A negative sentiment label means:", "The text matched a negative pattern worth a human look", ["The customer is wrong", "The agent must be coached today", "The trunk failed"], "Listen before you judge."),
        q("Sentiment replaces a quality form when:", "It does not. The form is still the rubric.", ["Always", "On CX 1", "On the Edge"], "QM and STA are different layers."),
        q("Sarcasm and unfortunate product names:", "Can produce a false sentiment hit", ["Are ignored by definition", "Disable ACD", "Change the region"], "Read the transcript."),
        q("The right next step after a negative filter is:", "Open the interaction", ["Delete the agent", "Disable recording", "Change the login host"], "The label is a pointer."),
        q("AI scoring’s token rules live on:", "The STA FAQ, which you re-read before budgeting", ["The SIP RFC", "The Edge group page", "A community dump"], "Do not invent a ratio."),
        q("Turning sentiment on for every queue with no reader:", "Creates a number nobody uses", ["Improves the service level", "Publishes flows", "Buys DIDs"], "Scope the queues you will review."),
    ],
    [("Label", "Not a verdict."), ("Listen", "Then coach."), ("Form", "Still QM."), ("Scope", "Only queues you will read.")],
    "Pick one queue",
    ["Name the queue.", "Say who reads negative hits each day.", "Name one phrase that would false-alarm.", "Say what they open before they coach."],
    "Someone owns the filter.",
    ("Score as verdict", "An agent is written up because one call was labeled negative. The customer was reading a product code.", "Sentiment: negative. Transcript: “order minus 4400”.", "Nobody opened the text.", "Require the transcript before any coaching note."),
))

add(lesson(
    "s-topics", "Topics, programs, and phrases are the dictionary", "Core", 12,
    "A program groups topics. A topic is phrases you expect to hear or read.",
    [
        "The STA overview describes topics and programs so you can find whether a phrase occurred: a competitor, a cancel request, a required disclosure. Phrases are the dictionary. If the phrase is not in the topic, the program will not find it, even when every agent said it.",
        "Start with a few phrases a supervisor can recite. A program with hundreds of unreviewed topics becomes a second language nobody maintains. Content search, in the next lesson, is how you test a phrase before you trust the topic.",
    ],
    cites("sta", "sta-about"),
    fig("Phrases make a topic. Topics sit in a program.", [
        ("ph", "Phrase", "architect", 16, 40),
        ("tp", "Topic", "wem", 46, 40),
        ("pr", "Program", "bot", 78, 40),
    ], [("ph", "tp"), ("tp", "pr")]),
    "Write a topic you could test tomorrow",
    [
        ("Sup", "Phrase", "The words customers actually use", "Not the legal name of the offer.", "Include the short form"),
        ("Admin", "Topic", "One intent", "Cancel, or disclosure, not both.", "Split if you must count them apart"),
        ("Admin", "Program", "The queue’s dictionary", "Assign it where transcription runs.", "An empty program is silence"),
        ("QA", "Test", "Search last week", "Did the phrase hit?", "Fix the dictionary before you publish a dashboard"),
    ],
    [
        q("A topic finds a phrase only if:", "The phrase is in the topic", ["The agent meant it", "The trunk is TLS", "The division is Home"], "The dictionary is the feature."),
        q("A program is:", "A grouping of topics", ["A SIP trunk", "A bullseye ring", "An OAuth grant"], "Keep the grouping small enough to maintain."),
        q("The best first phrases come from:", "How customers and agents actually talk", ["A trademark list nobody says", "The Edge hostname", "The exam catalog"], "Test them against real transcripts."),
        q("One topic that mixes cancel and a required disclosure:", "Makes the count useless for either question", ["Is required", "Saves tokens", "Sets utilization"], "Split intents you need to count apart."),
        q("A dashboard built before the dictionary is tested:", "Reports the dictionary’s gaps", ["Proves compliance", "Replaces QA", "Publishes the flow"], "Search first."),
        q("Topics do not replace:", "A recording policy or a quality form", ["The need to listen", "Both of those", "Nothing"], "They find interactions. They do not score them by themselves."),
    ],
    [("Phrase", "The words."), ("Topic", "One intent."), ("Program", "The dictionary for a queue."), ("Test", "Search before you trust a chart.")],
    "Draft one topic",
    ["Three phrases customers say.", "One phrase agents must say.", "The program name.", "How you will test it against last week."],
    "Each phrase is something a person would actually say.",
    ("Legal name only", "The disclosure topic hits twice a month. Agents say the short name all day.", "Topic phrase: the trademark. Agents say the nickname.", "The dictionary missed the floor.", "Add the nickname and re-count."),
))

add(lesson(
    "s-empathy", "Agent empathy is a detected behavior, still a form question", "Core", 11,
    "Empathy detection points at calls. Calibration still decides what empathy means for your company.",
    [
        "The STA material describes agent empathy as something you can detect and later filter on, including for process-automation style triggers when the current article lists that filter. It is a model’s reading of the agent’s language. Your quality form may define empathy differently: a pause, a repeated question, an offer.",
        "Use the detection to find calls for calibration. Do not let the model become the form. Two evaluators who disagree should score the same transcript, which is the calibration practice from the quality track.",
    ],
    cites("sta", "sta-faq", "qm"),
    fig("The model flags language. The form decides the score.", [
        ("ag", "Agent", "agent", 16, 40),
        ("em", "Empathy", "bot", 48, 40),
        ("fm", "Form", "wem", 80, 40),
    ], [("ag", "em"), ("em", "fm")]),
    "Put empathy on the form only if you can hear it",
    [
        ("QA", "Definition", "Write what empathy means here", "One sentence.", "The model does not read your sentence unless the question matches"),
        ("STA", "Filter", "Low empathy", "Pull five calls.", "Calibration set"),
        ("Team", "Score", "Same calls, two evaluators", "Compare.", "The QM article expects this"),
        ("Auto", "Trigger", "Only if the article lists the filter", "Re-read before you automate a coaching event.", "Do not invent a filter"),
    ],
    [
        q("Agent empathy detection is:", "A model’s reading of agent language", ["A guaranteed coaching outcome", "A trunk metric", "A license named CX 1"], "Treat it as a finding aid."),
        q("Your form’s definition of empathy:", "Can differ from the model. Calibration is how you notice.", ["Is illegal", "Must be deleted", "Is an RFC"], "Write the definition down."),
        q("Automating a coaching event on empathy:", "Requires the current article to list that filter", ["Is always on", "Needs an Edge", "Uses 911"], "Re-read the STA pages."),
        q("The calibration practice is:", "Two evaluators, one interaction", ["Two regions, one trunk", "Two OAuth clients", "Two number plans"], "That is the quality article’s tool."),
        q("A low-empathy flag with a kind transcript means:", "Look before you coach", ["The agent failed", "Delete the recording", "Disable STA"], "The flag is not the form."),
        q("Empathy detection does not remove the need for:", "A recording or transcript a human can open", ["Queues", "Both a recording and a person", "Agents"], "You cannot coach a score you cannot inspect."),
    ],
    [("Model", "Flags language."), ("Form", "Defines the behavior."), ("Calibrate", "Humans agree."), ("Automate", "Only with a documented filter.")],
    "Write the empathy sentence",
    ["Your definition.", "The five-call calibration plan.", "Whether a trigger is documented today.", "Who talks to the agent."],
    "The definition fits on one line a supervisor can say.",
    ("Auto-coach", "Agents get a coaching task every low-empathy flag, including calls where they followed the script.", "Trigger: empathy. No human review.", "The filter became the verdict.", "Route flags to a reviewer. Keep the form."),
    "Confirm the current trigger filters on the STA pages before you automate anything from empathy.",
))

add(lesson(
    "s-search", "Content search is how you test the dictionary", "Core", 11,
    "Search the transcript before you trust a topic count.",
    [
        "The STA pages describe content search so you can find interactions by what was said or written. Use it when a topic count looks wrong. Search the phrase. If search finds it and the topic does not, the dictionary is the bug. If search does not find it, the words were never in the transcript: wrong leg, transcription off, or people said something else.",
        "Search is also how a supervisor prepares a calibration set without guessing. Pull the interactions, then open them in quality management. Do not export customer text into a slide.",
    ],
    cites("sta", "sta-about", "qm"),
    fig("Search checks the words. The topic count comes after.", [
        ("tr", "Transcript", "bot", 18, 40),
        ("se", "Search", "architect", 50, 40),
        ("tp", "Topic", "wem", 80, 40),
    ], [("tr", "se"), ("se", "tp")]),
    "Debug a topic that will not hit",
    [
        ("Sup", "Search", "The exact phrase", "Quotes if the product search supports them.", "Read the current search help"),
        ("Result", "Hits", "Compare to the topic", "Search yes, topic no: dictionary.", "Search no: the words were not transcribed"),
        ("Admin", "Leg", "IVR versus agent", "The phrase may be in a leg you excluded.", "Scope lesson"),
        ("QA", "Set", "Five interactions", "Calibrate. Do not paste transcripts into chat.", "Customer text stays in the org"),
    ],
    [
        q("Search finds the phrase and the topic does not. The bug is:", "The topic dictionary", ["The carrier", "The login host", "Bullseye"], "The words exist. The topic missed them."),
        q("Search finds nothing. The likely checks are:", "Transcription on, the right leg, and the words people actually used", ["A new Edge group", "A concurrent peak", "An implicit grant"], "The text has to exist first."),
        q("Content search is a good way to:", "Build a calibration set", ["Replace the recording policy", "Buy numbers", "Set ACW"], "Then open the interactions in QM."),
        q("Pasting customer transcripts into a slide is:", "A data leak. Leave them in the org.", ["Required", "The export path", "Fair use"], "Search inside the product."),
        q("A topic used in a dashboard before search testing:", "May be counting the wrong dictionary", ["Is certified", "Is an RFC", "Sets the service level"], "Test the phrase."),
        q("Voicemail phrases missing from search can mean:", "That leg is outside the transcription scope you configured", ["SIP failed", "The queue has 5001 members", "ACW is optional"], "Check scope before you rewrite the topic."),
    ],
    [("Search", "Did the words exist?"), ("Topic", "Did the dictionary include them?"), ("Leg", "IVR, agent, voicemail."), ("Privacy", "Transcripts stay in the org.")],
    "Run the debug on paper",
    ["Write a phrase.", "Say what you conclude if search hits and the topic does not.", "Say what you conclude if search misses.", "Name where the calibration set lives."],
    "Both conclusions are different bugs.",
    ("Dashboard first", "Leadership reports zero cancel requests. Search finds “cancel my plan” all week.", "Topic phrase: “cancellation request”.", "The dictionary used the brochure.", "Add the words customers say."),
))

add(lesson(
    "s-timing", "Full analysis and a faster transcript are different clocks", "Advanced", 12,
    "Some views wait until the interaction is complete. A lower-latency transcript path is a different API.",
    [
        "The STA FAQ and overview distinguish analysis that completes after the interaction from lower-latency transcript delivery through the Notifications API. A supervisor refreshing a topic count during the call should not expect the final program result. A bot or a process that needs words sooner has to use the path the page documents for that latency, and only the filters the page lists.",
        "Process-automation triggers described alongside STA can filter on topic, sentiment, and empathy when those filters are on the page you open. Audio streaming to an outside processor is a separate design. Re-read before you name the connector. This lab does not invent a streaming vendor.",
    ],
    cites("sta", "sta-faq", "sta-about"),
    fig("Complete-interaction analysis and a notification transcript run on different clocks.", [
        ("call", "Call", "phone", 14, 40),
        ("note", "Notification", "architect", 46, 22),
        ("done", "Final analysis", "wem", 78, 58),
    ], [("call", "note"), ("call", "done")]),
    "Pick the clock before you automate",
    [
        ("Need", "Final topics", "After the interaction", "Program results settle then.", "Do not poll mid-call and call it truth"),
        ("Need", "Words sooner", "Notifications API", "The FAQ’s lower-latency path.", "Still not a license to invent events"),
        ("Need", "A trigger", "Only documented filters", "Topic, sentiment, empathy if the page lists them.", "Re-read"),
        ("Need", "Outside audio", "A documented streaming option", "Confirm the connector.", "Do not name one from memory"),
    ],
    [
        q("A topic count during the call may be:", "Incomplete, because full analysis follows interaction completion", ["The billing system", "Always final", "A bullseye ring"], "Wait for the clock the page describes."),
        q("Lower-latency transcripts are associated with:", "The Notifications API, as the FAQ describes", ["The Edge serial port", "RFC 4733 alone", "A personal mailbox"], "Use that path when you need words sooner."),
        q("A trigger filter you cannot find on the current page:", "Does not exist for your design", ["Is implied", "Is free", "Is CX 1"], "Follow the page."),
        q("Sentiment, topic, and empathy as trigger filters:", "Are usable when the current STA article lists them", ["Are always illegal", "Replace ACD", "Set utilization"], "Re-read before you automate."),
        q("Naming a streaming vendor from memory is:", "Out of scope for this lab", ["Required", "The same as content search", "A number plan"], "Confirm the connector article."),
        q("AI scoring still waits on:", "A transcript, plus QM and tokens", ["Only a notification ping", "Only sentiment", "Only a topic"], "The FAQ’s three gates remain."),
    ],
    [("Final", "After the interaction."), ("Sooner", "Notifications API."), ("Triggers", "Only listed filters."), ("Streaming", "Confirm the connector. Do not invent one.")],
    "Choose a clock",
    ["What the supervisor dashboard needs.", "What an automation needs.", "Which page you will re-read.", "The connector name you are deliberately not inventing."],
    "The two clocks are written down as different requirements.",
    ("Mid-call truth", "A wallboard shows zero empathy flags at second 20 and leadership pages the vendor.", "Interaction still active. Final analysis not run.", "The clock was wrong.", "Read the final program after completion, or use the documented notification path for words-sooner."),
    "AudioHook and other streaming connectors must be confirmed on the current article. This lesson does not rank vendors.",
))
