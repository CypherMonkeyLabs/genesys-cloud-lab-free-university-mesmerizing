from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "quality",
    "title": "Quality and speech analytics",
    "kicker": "Chapter",
    "accent": 3,
    "summary": "Evaluation forms, AI scoring, topics and programs, and the limits on the speech-analytics articles.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "y-qm", "Quality evaluates the interaction. Speech analytics reads it", "Foundation", 12,
    "The quality article says speech and text analytics runs on 100 percent of interactions. That is a claim to re-open, not a sample size you invent.",
    [
        "The about-quality-management article says quality management lets managers record and evaluate agents and interactions, and coach them. Its administration list includes evaluation forms, weights, policies, and exporting recordings to AWS. Its evaluation list includes a dashboard, scoring, calibration, monitoring in-progress interactions, annotations, assignees, and disputes. Coaching appointments are a separate section on that page.",
        "The same article says speech and text analytics provides automated analytics on 100 percent of interactions. This chapter uses that sentence as the article’s scope, not as a guarantee this lab measured. The quality track in the lab already walks forms, policies, and coaching at a high level. This chapter goes into the automation options, the topic dictionary, and the program limits.",
    ],
    cites("qm-article", "recording", "sta"),
    fig("Recording and a form are quality. Topics and sentiment are speech analytics.", [
        ("rec", "Recording", "wem", 16, 40),
        ("form", "Form", "agent", 46, 28),
        ("sta", "STA", "bot", 76, 55),
    ], [("rec", "form"), ("rec", "sta")]),
    "Point a question at one section",
    [
        ("Score", "Evaluations", "Form, calibration, dispute", "The article lists them.", "Do not invent the click path"),
        ("Coach", "Appointments", "A separate section", "Not the same object as a topic.", "Supervisors can create them"),
        ("Listen", "STA", "100 percent, as the article says", "Re-open the sentence before you quote it.", "Programs come later"),
        ("Store", "Export", "AWS is named", "This lab does not configure a bucket.", "Retention stays on the recording article"),
    ],
    [
        q("The quality article’s job for managers is:", "Record and evaluate agents and interactions, and coach", ["Forecast intervals", "Choose a SIP transport", "Issue an exam"], "Forecasting is the previous chapter."),
        q("Calibration, disputes, and annotations appear under:", "Evaluations", ["The forecast editor", "Direct routing", "Number plans"], "The article lists them in that section."),
        q("Speech and text analytics, on that quality article, covers:", "100 percent of interactions", ["A 20-pair sample", "Only bullseye calls", "Only the first 100 agents"], "Treat the sentence as the article’s, and re-open it."),
        q("Coaching on that page is:", "Appointments, in their own section", ["A bullseye ring", "A forecast creation method", "An OAuth grant"], "Do not fold coaching into a topic."),
        q("Exporting recordings, as the administration list names it, goes to:", "AWS", ["The Edge group", "A Wikipedia page", "The exam catalog"], "This lab does not create the bucket."),
        q("This chapter adds, beyond the existing quality track:", "Automation options, the topic dictionary, and program limits", ["A live organization login", "A price", "A sixth routing method"], "The earlier track remains the policy and coaching path."),
    ],
    [("QM", "Record, evaluate, coach."), ("Evaluations", "Forms through disputes."), ("STA", "100 percent, on that article."), ("Export", "AWS is the named store.")],
    "Sort six tasks",
    ["Publish a form.", "Hold a calibration.", "Compare a forecast.", "Add a topic.", "Open a dispute.", "Change a bullseye ring.", "Mark the ones that belong on the quality article."],
    "The forecast and the ring are not marked as quality tasks.",
    ("Hundred-percent sample", "A proposal promises a custom 10 percent sample because “analytics is a sample.”", "The quality article says 100 percent.", "The proposal reused a different product’s habit.", "Quote the article, then re-open it before the proposal is sent."),
))

add(lesson(
    "y-form", "A question is human, AI scored, or assisted by topics", "Foundation", 12,
    "The form article names three automation choices. Evaluation focus is Full Interaction or Evaluated Agent.",
    [
        "The create-and-publish article, as the automated-scoring article points at it, gives each question one of three choices: No Automation, AI Scoring, or Evaluation Assistance. No Automation is a person. AI Scoring is a model. Evaluation Assistance uses speech and text analytics topics to select the answer. Both AI Scoring and Evaluation Assistance support voice and digital interactions, on the automated-scoring article.",
        "When you add the question, that article also asks for an Evaluation Focus: Full Interaction or Evaluated Agent. Publishing is still required for the form to be used. The quality article’s list includes weights, copying a form, and assigning an evaluation. This lesson does not invent point values. If a weight is not on the page you have open, leave it off the design.",
    ],
    cites("qm-form", "qm-score", "qm-article"),
    fig("Three ways to answer. Focus says whose part of the interaction is in scope.", [
        ("no", "No automation", "agent", 16, 40),
        ("ai", "AI scoring", "bot", 48, 22),
        ("ea", "Assistance", "wem", 48, 68),
        ("foc", "Focus", "architect", 80, 40),
    ], [("no", "foc"), ("ai", "foc"), ("ea", "foc")]),
    "Label each question",
    [
        ("Human", "No Automation", "A person answers", "Still a published form.", "Weights stay on their article"),
        ("Model", "AI Scoring", "Voice and digital", "The next lesson is the confidence rule.", "Needs the permissions on that page"),
        ("Topics", "Evaluation Assistance", "Phrases match a topic", "All conditions must be true.", "One answer per question"),
        ("Scope", "Focus", "Full interaction or evaluated agent", "Pick one.", "Do not leave it implied"),
    ],
    [
        q("The three automation choices are:", "No Automation, AI Scoring, and Evaluation Assistance", ["Short-term, long-term, and blank", "Standard, bullseye, and preferred", "Voice, SMS, and email"], "Those three are on the automated-scoring setup."),
        q("Evaluation Assistance selects an answer from:", "Speech and text analytics topics", ["A forecast CSV", "A preferred-agent score", "A SIP response"], "AI Scoring is the model. Assistance is the topic conditions."),
        q("AI Scoring and Evaluation Assistance, on that article, support:", "Voice and digital interactions", ["Only fax", "Only forecasts", "Only direct-routing SMS"], "The article says both media types."),
        q("Evaluation Focus choices named in the setup are:", "Full Interaction and Evaluated Agent", ["Ring 1 and ring 2", "15 and 30 minutes", "CX 1 and CX 4"], "Set it when you add the question."),
        q("No Automation means:", "A person reviews and answers", ["The question is skipped", "Topics fill it", "The form cannot be published"], "Publishing is still how the form is used."),
        q("A weight that is not on the page you opened should be:", "Left out of the design", ["Copied from another form you remember", "Set to 100", "Stored as a skill proficiency"], "The quality article points at a weights article. Open that page before you type a number."),
    ],
    [("Three", "Person, model, or topics."), ("Focus", "Full interaction or evaluated agent."), ("Media", "Voice and digital, for the automated choices."), ("Weights", "Open the weights article.")],
    "Mark a five-question form",
    ["Two human questions.", "Two topic questions.", "One model question.", "The focus for the model question."],
    "Each question has one of the three labels, and the focus is written down.",
    ("Silent automation", "Every question is left on No Automation, and the design still says topics will fill the scores.", "Evaluation Assistance has to be selected on the question.", "The topic existed, so the form was assumed to use it.", "Set Evaluation Assistance on the answers that should move, and publish the form."),
))

add(lesson(
    "y-ai", "AI scoring waits for history, and a low week hides the answer", "Core", 14,
    "A rolling window of 25 submissions. Below 75 percent, the answer is hidden. The transcript needs 300 characters.",
    [
        "The automated-scoring article says AI scoring runs only when the conversation meets at least one of its criteria, and the criterion written in the notes this lab could read is a transcript of at least 300 characters. If the criteria are not met, it does not evaluate. Questions and each answer are limited to 500 characters. Help text is limited to 6,000. You can save at most five answer options. The model’s text must match an answer exactly, including accents.",
        "Accuracy is how often people change the AI answer. The window is the 25 most recent submissions for that question. At 75 percent or above, the answer is shown. Below 75 percent, the question is flagged low-confidence and the answer is hidden, while Genesys Cloud keeps storing the model’s response. The flag clears when the same window rises above 75 percent again. Republishing the form resets that history. History for a quiet question is deleted after 30 days without activity. The prerequisites named on the page are CX 1 WEM Add-on II, CX 2 WEM Add-on I, CX 2, CX 3, or CX 4, the evaluation-form permissions it lists, and AI Experience Tokens.",
    ],
    cites("qm-score", "qm-form", "overview"),
    fig("Twenty-five human edits decide whether the next evaluator sees the model’s answer.", [
        ("tr", "300 characters", "bot", 18, 40),
        ("win", "25 submissions", "wem", 52, 28),
        ("hide", "Under 75%", "agent", 52, 72),
    ], [("tr", "win"), ("win", "hide")]),
    "Decide if the model answer is visible",
    [
        ("Length", "Transcript", "At least 300 characters", "Otherwise this notes section says it does not evaluate.", "Do not add a second threshold from memory"),
        ("Window", "25", "Most recent submissions", "People overriding the answer lowers accuracy.", "Per question"),
        ("Show", "75 percent", "At or above, visible", "Below, hidden, still stored.", "The flag can return"),
        ("Reset", "Republish", "History clears", "30 quiet days delete it too.", "Tokens and the listed licenses"),
    ],
    [
        q("The transcript length this lesson will state, because it is the criterion readable on the notes, is:", "At least 300 characters", ["At least 30 words", "At least 7 days", "At least 500 topics"], "Other thresholds belong on the page only after you see them there."),
        q("Historical accuracy uses:", "The 25 most recent submissions for that question", ["The first 100 agents", "Six forecast weeks", "20 agent-score pairs"], "The article calls it a rolling window."),
        q("Below 75 percent in that window, Genesys Cloud:", "Hides the AI answer and flags low confidence, and still stores the response", ["Deletes the recording", "Publishes the form", "Switches the queue to bullseye"], "Above 75 percent, the answer is shown again."),
        q("Republishing the form:", "Resets the tracked history for questions with AI scoring", ["Keeps the 25 submissions", "Removes the topics", "Extends history to 130 weeks"], "A question with no activity for 30 days also loses its history."),
        q("The answer-option cap for an AI scoring question is:", "Five", ["Twenty", "Fifty", "One hundred"], "Questions and answers are 500 characters. Help text is 6,000."),
        q("Licenses named in the prerequisites include:", "CX 2, CX 3, CX 4, and the two WEM add-ons listed there, plus AI Experience Tokens", ["Only a BYOC trunk", "Only GC-GCP", "Only the Edge"], "Re-open the prerequisite list before you buy."),
    ],
    [("300 characters", "The transcript criterion this lab is willing to state."), ("25", "The rolling window."), ("75 percent", "Show above, hide below."), ("Reset", "Republish, or 30 quiet days.")],
    "Say whether the answer shows",
    ["A 200-character transcript.", "A 301-character transcript with 80 percent agreement over 25 submissions.", "The same question after someone republishes the form.", "The license line you still need to re-read."],
    "The short transcript does not evaluate, and the republish clears the streak.",
    ("Hidden and deleted", "A supervisor turns AI scoring off because the answer disappeared for a week, and deletes the question.", "Under 75 percent the answer is hidden and the response is still stored.", "The flag was read as a failure of the recording.", "Leave the question. Read the window. Fix the wording if people keep overriding it."),
    "This lesson states the 300-character criterion because that is the threshold written in the notes section opened in 2026-10. It does not add a seconds threshold.",
))

add(lesson(
    "y-topics", "Phrases make a topic. Topics make a program", "Core", 12,
    "A program is mapped to queues or flows, and it can turn sentiment and empathy on or off.",
    [
        "The programs, topics, and phrases article defines the dictionary. A phrase is a string of words for one way to say something, typed one by one or uploaded, and words outside the standard dictionary are added to the language model. A topic is a collection of phrases for a business intent, such as cancellation. A program is a package of topics mapped to queues or flows, and it may contain more than one language or dialect. The program can enable or disable customer sentiment analysis and agent empathy analysis for its own interactions.",
        "Evaluation Assistance uses those topics as conditions. The automated-scoring article says a topic cannot appear in more than one condition, and only one answer on a question can have assistance conditions. If several topics sit in one Includes condition, one match makes the condition true. If several sit in one Excludes condition, the condition is true only when all of them are absent. When a question has several conditions, every condition must be true before the answer is filled in.",
    ],
    cites("sta-dict", "sta-program", "qm-score"),
    fig("Phrases roll up to a topic. Topics roll up to a program on a queue or a flow.", [
        ("ph", "Phrase", "architect", 14, 40),
        ("tp", "Topic", "wem", 42, 40),
        ("pr", "Program", "bot", 70, 28),
        ("q", "Queue or flow", "queue", 70, 70),
    ], [("ph", "tp"), ("tp", "pr"), ("pr", "q")]),
    "Build one cancellation detector",
    [
        ("Phrase", "Words", "One way to cancel", "Upload or type.", "New words join the model"),
        ("Topic", "Intent", "The set of phrases", "Cancellation is the article’s example.", "Not a skill proficiency"),
        ("Program", "Package", "Queues or flows", "Sentiment and empathy are switches here.", "More than one dialect is allowed"),
        ("Form", "Conditions", "All must be true", "One answer only.", "A topic is used once"),
    ],
    [
        q("A topic is:", "A collection of phrases for a business intent", ["A bullseye ring", "A forecast week", "An OAuth scope"], "The cancellation example is on the dictionary article."),
        q("A program tells speech analytics:", "Which topics to look for, on the queues or flows it is mapped to", ["Which trunk to use", "Which exam to sit", "Which forecast method to run"], "It can also switch sentiment and empathy for those interactions."),
        q("Words that are not in the standard dictionary:", "Can be put in a phrase and are added to the language model", ["Are rejected", "Become wrap-up codes", "Disable the program"], "The phrases article says that."),
        q("Several conditions on one assisted answer are filled in when:", "Every condition is true", ["Any one condition is true", "The forecast overlaps", "The agent is preferred"], "The scoring article says all of them."),
        q("An Includes condition with three topics is true when:", "One of those topics is found", ["All three are found", "None are found", "The transcript has 300 characters"], "An Excludes condition with several topics is true only when all of them are absent."),
        q("A topic used in two evaluation-assistance conditions is:", "Not allowed", ["Required", "Only valid on bullseye", "How you publish a program"], "And only one answer on the question gets those conditions."),
    ],
    [("Phrase", "One way of saying it."), ("Topic", "The intent."), ("Program", "Topics on queues or flows."), ("Conditions", "All true, one answer, one use of each topic.")],
    "Write a three-layer example",
    ["Two phrases.", "The topic name.", "The queue or flow on the program.", "One Includes condition and what makes it true."],
    "The Includes condition does not require every topic if several were selected.",
    ("Both phrases required", "A form is built so the answer appears only when every cancellation phrase is spoken.", "An Includes condition with several topics is true when one of them is found.", "The condition was read as an all-skills match.", "Use one topic that contains the phrases, or separate conditions if you truly need all of them."),
))

add(lesson(
    "y-limits", "Programs have counts, and the organization switch wins", "Advanced", 14,
    "One hundred programs. Five hundred topics per dialect. Twenty scoring rules. Sentiment off at the org turns it off everywhere.",
    [
        "The work-with-a-program article’s create section states these limits: 100 programs in the organization, 20 tags on a program and on a topic, 500 queues and 500 flows on one program, and 20,000 queues and flows for the whole system. The program name is case sensitive and limited to 100 characters. The description is limited to 10,240 characters. A tag name is case sensitive and limited to 100 characters. Topic limits on the same article: 500 topics per dialect, 15 dialects in the editor, and you cannot publish a program that contains more than 500 unpublished topics. A program can include up to 20 enabled agent-scoring rules.",
        "You save a draft, then publish. The program uses the topic version that was current at publish time. A default program with predefined topics is included. Quality administrators can manage queues, flows, and scoring, and cannot change speech and text analytics settings. In Genesys Cloud EX, programs map to queues only; picking a flow has no effect. Customer sentiment and agent empathy are on by default. If either is disabled for the organization, the program control is unavailable and the analysis does not run, while the program’s own saved choice is kept for later.",
    ],
    cites("sta-program", "sta-dict"),
    fig("Publish uses the topic version from that moment. The organization switch overrides the program.", [
        ("dr", "Draft", "architect", 16, 40),
        ("pub", "Publish", "wem", 48, 40),
        ("org", "Org switch", "region", 80, 40),
    ], [("dr", "pub"), ("org", "pub")]),
    "Check a program against the counts",
    [
        ("Size", "100 programs", "500 topics per dialect", "15 dialects.", "20 scoring rules"),
        ("Map", "500 queues and 500 flows", "20,000 combined in the system", "EX ignores flows.", "Name is 100 characters"),
        ("Publish", "Draft first", "Topic version is frozen then", "More than 500 unpublished topics cannot publish.", "A default program already exists"),
        ("Switch", "Org off", "Overrides the program", "The program value is kept.", "Quality admins do not edit STA settings"),
    ],
    [
        q("The maximum number of programs on that article is:", "100", ["15", "500", "20,000"], "500 is the per-program queue cap and the per-dialect topic cap. 20,000 is the system total of queues and flows."),
        q("Topics per dialect are capped at:", "500", ["20", "100", "15"], "The editor also limits you to 15 dialects."),
        q("Enabled agent-scoring rules on one program:", "Up to 20", ["Up to 5", "Up to 100", "Unlimited"], "Tags are also capped at 20, on both programs and topics."),
        q("Publishing uses:", "The topic version applied at publish time", ["Whatever the topic says the next morning", "The forecast", "The queue routing method"], "Save a draft before you publish."),
        q("If the organization disables sentiment:", "Analysis does not run, even if the program still has it enabled", ["The program override wins", "Only EX is affected", "Topics are deleted"], "The program’s setting is kept so you can turn it on again later."),
        q("In Genesys Cloud EX, a flow selected on a program:", "Has no effect, because programs map to queues", ["Replaces the queue", "Enables bullseye", "Publishes an Architect bot"], "The article says every flow type may appear in the editor."),
    ],
    [("100", "Programs."), ("500", "Topics per dialect, and queues or flows on one program."), ("20", "Tags, and enabled scoring rules."), ("Org", "An off switch overrides the program.")],
    "Reject three designs",
    ["Program 101.", "A dialect with 501 topics.", "Sentiment on in the program and off in the organization, with a note that analysis will still run.", "The note you write instead."],
    "The third design says analysis will not run.",
    ("Flow in EX", "An EX program is mapped to a flow and the team expects those calls to be tagged.", "The article says EX programs assign to queues and a selected flow has no effect.", "The editor showed the flow types.", "Map the queues. Leave the flow selection out of the EX design."),
))

add(lesson(
    "y-score", "Agent scoring picks which agent receives the evaluation", "Advanced", 12,
    "Each, first, or last matched agent. The article also says the last participant is the evaluated agent.",
    [
        "The program article’s agent-scoring section lists three generation choices: Each Matched Agent creates an evaluation for every matched agent, First Matched Agent only the first, and Last Matched Agent only the last. A later sentence on the same page says the last agent to participate is assigned as the evaluated agent. Read both sentences against the control you are about to set, because this lab will not collapse them into one rule.",
        "Automated scoring there uses a published agent auto-evaluation form. For digital interactions, the article says evaluations are regenerated when a new response is added to the thread. Calibration, disputes, and coaching remain the quality article’s process names. This lesson does not invent a calibration agenda. The quality track is where the coaching loop is practiced.",
    ],
    cites("sta-program", "qm-article", "qm-score"),
    fig("The program decides who is scored. The form is already published.", [
        ("rule", "Rule", "wem", 18, 40),
        ("who", "Which agent", "agent", 52, 40),
        ("form", "Published form", "architect", 84, 40),
    ], [("rule", "who"), ("who", "form")]),
    "Pick who is evaluated",
    [
        ("Each", "Every matched agent", "A separate evaluation", "Use it when transfers matter.", "More evaluations"),
        ("First", "First matched agent", "One evaluation", "The opener.", "Not the closer"),
        ("Last", "Last matched agent", "One evaluation", "The page also says the last participant is assigned.", "Confirm the control"),
        ("Digital", "New response", "Regenerate", "The thread changed.", "The form must already be published"),
    ],
    [
        q("Each Matched Agent means:", "A separate evaluation for every matched agent", ["One evaluation for the queue", "A forecast per agent", "A topic per phrase"], "First and Last each produce one evaluation."),
        q("A published form is required because:", "The scoring rule selects a published agent auto-evaluation form", ["Drafts are scored automatically", "Topics replace the form", "The Edge stores the form"], "Publish the form before you expect scores."),
        q("The two “last agent” sentences on the program article should be:", "Read against the control you set, not merged by this lab", ["Ignored", "Treated as a bullseye cap", "Copied into a forecast"], "One is a generation choice. Another sentence assigns the last participant."),
        q("A new digital response:", "Regenerates the automated evaluation", ["Freezes the first score", "Deletes the program", "Starts a schedule"], "The article says the score follows the latest transcript context."),
        q("Calibration is:", "Named on the quality article, and not given a timetable in this lesson", ["A forecast method", "A ring delay", "An OAuth grant"], "Open the calibration article before you write the meeting."),
        q("Quality administrators, on the program article, cannot:", "Change speech and text analytics settings", ["Manage queues on the program", "Manage flows on the program", "Manage agent scoring"], "Speech and text analytics administrators have the STA settings."),
    ],
    [("Each", "One evaluation per matched agent."), ("First or last", "One evaluation."), ("Digital", "Regenerate when the thread grows."), ("STA settings", "Not a quality-admin edit.")],
    "Choose a rule for a transfer",
    ["The customer spoke to two agents.", "You want both scored.", "You want only the closer.", "The sentence you will re-read before you trust “last.”"],
    "Both-scored uses Each. Closer-only uses Last, with the confirm note.",
    ("One score for two agents", "A transfer is scored once, on the first agent, and the closer never sees a form.", "The rule was First Matched Agent.", "Each was what the quality team asked for.", "Change the rule to Each Matched Agent and confirm the published form."),
    "The program article lists Each, First, and Last Matched Agent, and also says the last agent to participate is assigned as the evaluated agent. Confirm which control you are setting.",
))
