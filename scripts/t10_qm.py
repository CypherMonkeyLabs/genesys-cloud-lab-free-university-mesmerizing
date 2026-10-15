from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "qm",
    "title": "Quality and recording",
    "kicker": "WEM",
    "accent": 3,
    "summary": "Evaluation forms, calibration, coaching, recording policies, and the prerequisites for AI scoring.",
    "lessons": [],
}
def add(item):
    TRACK["lessons"].append(item)

add(lesson(
    "m-overview", "Quality management evaluates the conversation", "Core", 11,
    "QM records and scores interactions, and it can coach. It is not the schedule.",
    [
        "The quality article describes evaluation forms, policies, calibration, coaching, disputes, and the ability to evaluate in-progress or recorded interactions. Speech and text analytics can cover the conversations so a form is not the only way you learn what was said. Screen recording is a separate capability for the agent’s screen during ACD interactions.",
        "The 2023 feature-matrix summary showed quality on the packages that include it, and the current overview puts that quality layer on CX 2 and above. WFM remains CX 3. Do not tell a CX 2 customer they have scheduling because they have evaluations.",
    ],
    cites("qm", "recording", "overview"),
    fig("Evaluate the interaction. Schedule the people somewhere else.", [
        ("rec", "Recording", "wem", 18, 40),
        ("form", "Form", "wem", 48, 40),
        ("coach", "Coaching", "agent", 78, 40),
    ], [("rec", "form"), ("form", "coach")]),
    "Open QM without opening WFM",
    [
        ("Admin", "Policy", "Which calls", "Recording policy selects them.", "Not every call by accident"),
        ("Admin", "Form", "Questions and weights", "The score is the form.", "Calibration keeps evaluators honest"),
        ("Sup", "Coach", "Appointment", "The article includes coaching.", "A score without a conversation is a number"),
        ("Scope", "Package", "CX 2 for QM, CX 3 for WFM", "They are not the same row.", "Read the overview"),
    ],
    [
        q("Quality management’s article includes:", "Forms, policies, calibration, coaching, and disputes", ["SIP trunks", "Edge groups", "Number plans"], "Those are the QM tools."),
        q("Screen recording is:", "The agent’s screen during ACD interactions", ["The caller’s camera by default", "A trunk subtype", "A token"], "About recording says so."),
        q("CX 2 and CX 3 differ here because:", "QM is in the CX 2 story. WFM arrives at CX 3.", ["They are identical", "CX 2 has no voice", "CX 3 removes QM"], "The overview stacks them."),
        q("A recording policy decides:", "Which ACD calls are recorded and how long they are kept", ["The bullseye delay", "The login host", "The exam code"], "About recording describes policies."),
        q("Evaluating an in-progress interaction is:", "Supported by the QM article", ["Forbidden", "A premises-only feature", "An RFC"], "The article lists in-progress evaluation."),
        q("Coaching appointments are for:", "Helping the agent improve after you know the gap", ["Buying DIDs", "Migrating DCVP", "Issuing OAuth secrets"], "The article includes them."),
    ],
    [("Forms", "The score."), ("Policy", "What gets recorded."), ("Coach", "What you do with the score."), ("Package", "QM from CX 2. WFM from CX 3.")],
    "Name the three objects",
    ["A policy.", "A form.", "A coaching use.", "The package for each of QM and WFM."],
    "The three objects are distinct.",
    ("Schedule sold as QM", "The customer bought CX 2 and expects forecasts.", "Overview: forecasts are WEM, CX 3.", "Quality was the CX 2 addition.", "Correct the order, or add the package that contains WFM."),
))

add(lesson(
    "m-form", "Forms have questions and weights", "Core", 11,
    "The form is the rubric. Weights decide which questions move the score.",
    [
        "The QM article points at evaluation form weights and at creating forms. A form that weights greeting at 80 percent and resolution at 5 percent will congratulate short polite calls that do not solve the problem. AI scoring, later, can answer some questions only when the interaction is transcribed and you have the tokens. The rubric still has to be one a human accepts.",
        "Calibration is how you find out that two evaluators do not mean the same thing by “empathy.” The article lists calibration as its own activity. Skipping it makes the leaderboard a measure of who graded, not of what happened.",
    ],
    cites("qm", "sta-faq"),
    fig("Weights decide the score. Calibration decides the graders agree.", [
        ("q1", "Question", "wem", 20, 40),
        ("w", "Weight", "architect", 48, 40),
        ("cal", "Calibration", "agent", 78, 40),
    ], [("q1", "w"), ("w", "cal")]),
    "Write a form you could defend",
    [
        ("Admin", "Questions", "Behavior you can hear", "Not a vibe.", "The transcript or the recording has to show it"),
        ("Admin", "Weights", "Resolution heavier than greeting", "Unless policy says otherwise.", "Write the reason"),
        ("Team", "Calibration", "Score the same call", "Compare.", "The article expects this"),
        ("AI", "Later", "Only some questions", "Tokens, STA, and QM are all required.", "The FAQ says so"),
    ],
    [
        q("Form weights matter because:", "They decide which questions move the score", ["They set the SIP codec", "They set ring count", "They buy numbers"], "A heavy greeting weight hides a missed resolution."),
        q("Calibration exists to:", "See whether evaluators score the same call the same way", ["Move the AWS region", "Publish a flow", "Reset utilization"], "The QM article lists it."),
        q("AI scoring still needs a form a human accepts because:", "The rubric is the definition of quality", ["AI ignores forms", "Tokens replace questions", "STA deletes weights"], "The FAQ ties AI scoring to evaluation questions."),
        q("A question the recording cannot show is:", "A bad question", ["The best question", "Required", "A trunk setting"], "Score what the interaction contains."),
        q("Screen recording helps a form when:", "The behavior is on the screen, not in the audio", ["You need RTP", "You need a PSAP", "You need a token only"], "About recording separates screen and call recording."),
        q("Two evaluators ten points apart on empathy means:", "Calibrate before you rank agents", ["Delete the form", "Disable recording", "Change regions"], "The gap may be the graders."),
    ],
    [("Weight", "What moves the score."), ("Calibrate", "Graders must agree."), ("Observable", "If it is not in the interaction, do not score it."), ("AI", "Does not replace the rubric.")],
    "Draft four questions",
    ["Two weighted behaviors.", "The heavier one.", "How you would calibrate.", "Which question could not be heard on audio alone."],
    "The heavier question is the one leadership claims to care about.",
    ("Greeting theater", "Top agents have short calls and perfect scores. Customers call back.", "Greeting weight: 70. Resolution weight: 5.", "The form rewards the wrong behavior.", "Reweight and recalibrate."),
))

add(lesson(
    "m-policy", "Recording policies choose calls and retention", "Core", 11,
    "A policy decides which ACD calls are recorded and how long they are kept. A secure flow is a hole in a segment, not a substitute for the policy.",
    [
        "About recording says you use policies to choose ACD calls and retention, and that a user can also record their own calls. Screen recording is specifically the agent’s screen during ACD interactions. Retention is a legal and a storage question. Storage is also a fair-use meter. Keep the policy’s duration and the fair-use page in the same review.",
        "A secure payment flow stops recording for that entry. It does not set retention for the rest of the call. QM cannot evaluate audio you never recorded. If the policy records nothing, the form has nothing to play.",
    ],
    cites("recording", "create-flow", "fair"),
    fig("Policy selects the call. Retention decides how long it lives.", [
        ("call", "Call", "phone", 16, 40),
        ("pol", "Policy", "wem", 46, 40),
        ("keep", "Retention", "region", 78, 40),
    ], [("call", "pol"), ("pol", "keep")]),
    "Write the policy in one paragraph",
    [
        ("Admin", "Who", "Which queues", "Not the whole org by default unless you mean it.", "Queues are the usual scope"),
        ("Admin", "How long", "Retention", "Match the legal hold.", "Storage is metered"),
        ("Admin", "Screen", "On or off", "Separate from the audio policy.", "ACD screen time"),
        ("Secure", "Segment", "Still a hole", "Payment digits stay out.", "The rest follows the policy"),
    ],
    [
        q("Call recording policies control:", "Which ACD calls are recorded and retention", ["Bullseye rings", "Login hosts", "Exam vouchers"], "About recording says so."),
        q("Screen recording records:", "The agent’s screen during ACD interactions", ["The caller’s desktop by default", "The carrier’s SBC", "The PSAP"], "That is the article’s scope."),
        q("A secure flow and a recording policy:", "The flow can suppress a segment. The policy still governs the call.", ["They are the same switch", "The flow sets retention", "The policy collects card numbers"], "Do not collapse them."),
        q("Retention that ignores fair use can:", "Become a storage overage", ["Delete the region", "Disable SIP", "Publish flows"], "Storage is a metered family on the policy page."),
        q("QM with a policy that records nothing:", "Has no audio to evaluate", ["Scores from the trunk name", "Uses bullseye", "Uses 988"], "The form needs the interaction."),
        q("Users recording their own calls is:", "Also described on the recording article", ["Forbidden", "CX 4 only", "A bot feature"], "The article mentions user recording separately from ACD policy."),
    ],
    [("Policy", "Which calls, how long."), ("Screen", "Agent screen, ACD."), ("Secure", "A segment, not the policy."), ("Storage", "A fair-use meter.")],
    "Draft the policy",
    ["Queues in scope.", "Retention.", "Whether screens are included.", "What the secure flow still hides."],
    "Legal and storage owners could both sign it.",
    ("Record everything forever", "Storage overage arrives, and a customer asks for a deletion you cannot map.", "Policy: all calls, no end date.", "Retention was not a decision.", "Set a duration with legal, then re-read the fair-use storage row."),
))

add(lesson(
    "m-coach", "Coaching and disputes close the loop", "Core", 11,
    "A score that the agent cannot see and cannot dispute is not a quality program.",
    [
        "The QM article lists coaching appointments, evaluation disputes, and managing those disputes. It also lists monitoring and coaching in-progress interactions. The point of the form is a conversation with the agent. A hidden score changes nothing on the next call.",
        "Disputes are not a failure of the form. They are how you find a bad question or a bad grade. Calibration feeds the same loop. If every dispute is denied in a minute, agents will stop reading the form.",
    ],
    cites("qm"),
    fig("Score, show, coach, and allow a dispute.", [
        ("s", "Score", "wem", 16, 40),
        ("a", "Agent", "agent", 42, 40),
        ("c", "Coach", "wem", 68, 22),
        ("d", "Dispute", "architect", 68, 70),
    ], [("s", "a"), ("a", "c"), ("a", "d")]),
    "Run one coaching week",
    [
        ("Eval", "Form", "Complete it", "On a recorded or in-progress interaction.", "The article allows both"),
        ("Agent", "Read", "They can see it", "Otherwise there is no program.", "Hidden scores do not coach"),
        ("Sup", "Appointment", "A real meeting", "The article’s coaching object.", "Not a drive-by"),
        ("Agent", "Dispute", "A path exists", "Manage it.", "Use it to fix the form"),
    ],
    [
        q("Coaching appointments are:", "A documented QM feature", ["A WFM activity only", "A trunk setting", "An RFC"], "The QM article lists them."),
        q("Disputes exist so that:", "Agents can challenge a grade, and you can find a bad rubric", ["Agents can delete recordings", "Agents can change regions", "Agents can skip On Queue"], "The article includes dispute management."),
        q("In-progress evaluation means:", "You can score while the interaction is still live", ["You must wait 30 days", "You must use a bot", "You must use BYOC"], "The article lists it."),
        q("A score the agent never sees:", "Does not change the next call", ["Is the recommended design", "Is required for AI", "Publishes the flow"], "Coaching needs a recipient."),
        q("Denying every dispute instantly will:", "Teach agents the form is not real", ["Improve calibration", "Fix weights", "Lower storage"], "Disputes are a feedback path."),
        q("Monitoring in-progress interactions is:", "Also on the QM article, beside coaching", ["Removed", "Premises only", "A number plan"], "The article lists monitor and coach."),
    ],
    [("Show the score", "Or it does not coach."), ("Appointment", "A real meeting."), ("Dispute", "A path, not a threat."), ("In progress", "Allowed.")],
    "Script one coaching session",
    ["The behavior.", "The evidence in the recording.", "The next-call change.", "How a dispute would be handled."],
    "The session cites a moment in the interaction, not a personality.",
    ("Score with no tape", "The agent disputes a failing grade and there is no recording.", "Policy recorded nothing. Form was filled from memory.", "There is no evidence.", "Turn on a policy for that queue before you score it."),
))

add(lesson(
    "m-ai", "AI scoring needs STA, QM, and tokens", "Advanced", 12,
    "The FAQ is blunt: AI scoring requires Speech and Text Analytics, Quality Management, and AI Experience Tokens.",
    [
        "The STA FAQ says AI scoring needs the interaction transcribed, and that Virtual Supervisor AI scoring needs STA, QM, and AI Experience Tokens. It also says one token covers 20 evaluations analyzed with AI scoring. Agent Copilot summaries are not billed a second time when Virtual Supervisor shows the same summary. Those are billing rules, and the FAQ is the source. Re-read the token ratio before you model a budget. This sentence is a pointer, not a quote you should freeze if the FAQ changes.",
        "AI scoring answers form questions. It does not replace calibration. A model that grades a question your form defines badly will do it consistently and wrongly. Fix the question.",
    ],
    cites("sta-faq", "qm", "copilot", "overview"),
    fig("Transcript plus form plus tokens, then a score.", [
        ("t", "Transcript", "bot", 16, 40),
        ("f", "Form", "wem", 46, 40),
        ("k", "Tokens", "region", 74, 40),
    ], [("t", "f"), ("f", "k")]),
    "Turn on AI scoring without a surprise bill",
    [
        ("Admin", "STA", "Transcription on", "No transcript, no score.", "The FAQ requires it"),
        ("Admin", "QM", "A form", "Questions the model can answer.", "Weights still matter"),
        ("Admin", "Tokens", "AI Experience Tokens", "The third prerequisite.", "CX 4’s token story is on the overview"),
        ("Finance", "Ratio", "Re-read the FAQ", "The 20-evaluations note lives there.", "Copilot summaries are not double-billed"),
    ],
    [
        q("AI scoring requires:", "STA, QM, and AI Experience Tokens", ["Only a queue", "Only an Edge", "Only GC-GCP"], "The FAQ lists all three."),
        q("Without transcription:", "AI scoring cannot evaluate the call", ["It uses the trunk name", "It uses bullseye", "It uses the division"], "The FAQ says transcription is required."),
        q("The FAQ’s token note for AI scoring is:", "1 token covers 20 evaluations. Re-read before you budget.", ["1 token covers 1 year", "Tokens are free", "Tokens replace QM"], "Treat the number as page content that can change."),
        q("Agent Copilot already summarized the interaction. Virtual Supervisor showing it:", "Does not bill a second summary, per the FAQ", ["Always bills double", "Deletes the recording", "Disables STA"], "The FAQ says you are not billed twice."),
        q("A badly written form question scored by AI:", "Will be consistently wrong", ["Will fix itself", "Will delete the question", "Will change the region"], "Calibrate the rubric."),
        q("CX 4’s published tokens relate to this how?", "The overview includes tokens on CX 4. The FAQ says scoring consumes them.", ["Tokens are only for SIP", "CX 1 includes unlimited scoring", "Tokens are activity codes"], "Read both pages."),
    ],
    [("Three gates", "STA, QM, tokens."), ("Ratio", "See the FAQ. Do not freeze it blindly."), ("No double bill", "Copilot summary reused by Virtual Supervisor."), ("Rubric", "Still yours.")],
    "Check the three gates",
    ["Is transcription on for the queue?", "Does a form exist?", "Do you have tokens?", "Did you re-read the FAQ’s ratio?"],
    "All three gates are yes, or you are not turning it on.",
    ("Score with no transcript", "AI scoring returns nothing useful.", "Voice transcription: off. Tokens: purchased.", "The FAQ requires the transcript.", "Enable transcription, then score."),
))

add(lesson(
    "m-export", "Retention, export, and the reason you recorded", "Advanced", 11,
    "Export and AWS recording paths exist so a recording can leave the platform under a policy, not as a side copy.",
    [
        "The QM article mentions AWS recording export among the tools around evaluations. About recording points at related articles for listening and for S3-style recording paths. Any export is still personal data. The fair-use storage meter and your retention policy decide how long the original lives. An export bucket you never expire is a second retention policy you forgot to write.",
        "Do not export “for a demo” from a production queue. Use a lab queue and a lab policy. The recordings in this lab’s incidents are synthetic text, not audio from a person.",
    ],
    cites("qm", "recording", "fair"),
    fig("Export is a second copy. It needs its own retention.", [
        ("g", "Genesys", "wem", 22, 40),
        ("x", "Export", "region", 55, 40),
        ("b", "Bucket", "crm", 84, 40),
    ], [("g", "x"), ("x", "b")]),
    "If you export, write the rule",
    [
        ("Legal", "Why", "A reason", "QA, dispute, or a legal hold.", "Not curiosity"),
        ("Admin", "Where", "The documented export path", "The QM article points at AWS export.", "Follow the current article"),
        ("Admin", "How long", "Bucket lifecycle", "Match or shorten the Genesys retention.", "Do not keep forever by default"),
        ("Lab", "Never", "Production audio in a demo", "Synthetic logs only in this lab.", "Real audio stays in the org"),
    ],
    [
        q("An export bucket without a lifecycle is:", "A second retention policy you did not mean to write", ["Free", "Required by RFC 3550", "A bullseye ring"], "Copies need an end date."),
        q("The QM article’s export mention is:", "AWS recording export, as a documented path", ["Email to a personal inbox", "A SIP REFER", "A quiz"], "Use the product path."),
        q("Fair use relates because:", "Storage is metered, and a copy does not make the original free", ["Exports are unlimited", "Exports delete tokens", "Exports are queues"], "Read the storage row."),
        q("This lab’s incident logs are:", "Synthetic text, not customer audio", ["Production recordings", "Carrier captures", "PSAP audio"], "Do not confuse them."),
        q("A secure-flow segment should be:", "Absent from the export as well, if it was never recorded", ["Added back from memory", "Stored in participant data", "Sent to the agent"], "You cannot export what the secure flow kept out."),
        q("The right queue for a vendor demo is:", "A lab queue with a lab policy", ["The production billing queue", "The emergency route", "The Home division’s only queue"], "Do not demo on real customers."),
    ],
    [("Reason", "Why the copy exists."), ("Lifecycle", "When the copy dies."), ("Meter", "Storage still counts."), ("Lab", "Synthetic here. Real audio stays in the org.")],
    "Write an export rule",
    ["The reason.", "The bucket lifecycle.", "Who can read it.", "A sentence that production audio is out of scope for demos."],
    "The rule has an end date.",
    ("Inbox forward", "Recordings arrive in a personal mailbox.", "No policy. An agent forwards the player link.", "That is not the export path, and it has no retention.", "Stop the forward. Use the documented export if a copy is justified, with a lifecycle."),
))
