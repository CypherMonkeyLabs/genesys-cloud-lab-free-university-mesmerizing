from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "predictive",
    "title": "Predictive Engagement",
    "kicker": "On the site",
    "accent": 3,
    "summary": "Website journeys, segments, action maps, Messenger, and the Journey Outcomes deprecation. This is not ACD predictive routing.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "pe-what", "Predictive Engagement watches the site, not the queue math", "Core", 13,
    "It predicts what a visitor is trying to do and offers a message, a chat, content, or a flow. Predictive routing is a different feature on the queue.",
    [
        "The About Predictive Engagement page calls it a Genesys Cloud AI feature that analyzes how visitors behave on websites, predicts the outcomes they are trying to reach, and personalizes the engagement. The use-case page says it uses machine learning, segmentation, and real-time outcome scoring, then engages with chat, a chatbot, or a content offer. You can also hand the moment to an Architect flow. None of that is the ACD routing method named predictive routing.",
        "Agents later see journey information on the interaction. Supervisors get visitor activity and action-map performance. Those reports sit beside contact-center analytics. They do not replace service level on the queue. Read the deprecation notice before you design anything that depends on Journey Outcomes. That feature has a planned end.",
    ],
    cites("pe-about", "pe-usecase", "pe-deprecate", "routing"),
    fig("The website is a separate door from the SIP trunk.", [
        ("web", "Website", "crm", 12, 40),
        ("pe", "Predictive", "bot", 40, 40),
        ("map", "Action map", "architect", 66, 28),
        ("q", "Queue", "queue", 88, 55),
    ], [("web", "pe"), ("pe", "map"), ("map", "q")]),
    "Keep the two predictives apart",
    [
        ("Visitor", "Site", "Page views and events", "Tracked by Predictive Engagement.", "Not a trunk"),
        ("Map", "Offer", "Message, chat, content, or flow", "The action types on the create page.", "Queue only if you route the offer"),
        ("Agent", "Journey", "Context on the interaction", "The about page lists that work.", "Not Copilot"),
        ("Queue", "ACD", "Predictive routing", "A different article.", "Do not mix the names"),
    ],
    [
        q("Predictive Engagement primarily watches:", "Visitors on your website", ["SIP trunks", "Edge groups", "Exam vouchers"], "The about page is about website behavior."),
        q("Predictive routing is:", "An ACD method on a queue", ["The same screen as action maps", "A Messenger snippet", "A forecast"], "The routing track is the other feature."),
        q("The use case names these engagement styles:", "Chat, chatbot, or content offer", ["A premises Edge", "A number plan", "A bullseye ring"], "An Architect flow is an additional action type on the create page."),
        q("A healthy queue with no website tracking means:", "Predictive Engagement has nothing to score", ["ACD is down", "TLS 5061 is closed", "The org moved regions"], "The site has to be instrumented."),
        q("Journey data shown to an agent is:", "Context on the interaction", ["A replacement for wrap-up codes", "The emergency route", "A client-credentials token"], "The about page lists working the interaction with journey information."),
        q("You should design a new Journey Outcome in October 2026 because:", "You should not. Read the deprecation first.", ["The feature is guaranteed permanent", "CX 1 includes it", "It opens RTP"], "The announcement tells you to avoid new outcome configurations."),
    ],
    [("Site", "Visitor behavior."), ("Not ACD", "Predictive routing is the queue method."), ("Offers", "Messaging, chat, content, flow."), ("Outcomes", "On a published deprecation.")],
    "Name the feature you mean",
    ["Write Predictive Engagement or predictive routing, not “predictive.”", "Name the site you would track.", "Name the offer type.", "Say whether a queue is involved."],
    "The four names do not collapse into one product.",
    ("One word for two products", "A design says “turn on predictive” and nobody knows which admin page to open.", "The queue uses standard routing. The website has no snippet.", "The names were swapped.", "Split the requirement into an action map or a queue routing method."),
))

add(lesson(
    "pe-track", "Messenger tracks web messaging. The old snippet tracks web chat.", "Core", 14,
    "Genesys tells Genesys Cloud CX customers to use web messaging. Leaving both snippets on the page double-counts the visit.",
    [
        "The about page says you can use web messaging with Predictive Engagement and encourages web messaging instead of web chat. The tracking-snippet article is explicit: web chat deploys the Predictive Engagement tracking snippet; web messaging deploys the Messenger snippet. Paste a tracking snippet in the head of the main window, not in an iframe. After ac('init') on a traditional snippet, or ac('load') on the SPA snippet, Predictive Engagement tracks pageview events.",
        "The migration article tells you to remove the tracking snippet when you deploy Messenger, because Digital User Tracking is already part of Messenger and two snippets double-track. Enable Digital User Tracking on the Messenger configuration, publish a new version, and point action maps that still say web chat at web messaging. The Messenger article says to turn on the Predictive Engagement toggle in the Apps tab when you want journey data, then use Live Now to see events.",
    ],
    cites("pe-about", "pe-snippet", "pe-migrate", "pe-messenger"),
    fig("One snippet on the page. Messenger replaces the legacy tracker for web messaging.", [
        ("old", "Legacy snippet", "phone", 18, 62),
        ("msg", "Messenger", "bot", 50, 28),
        ("live", "Live Now", "wem", 84, 40),
    ], [("msg", "live")]),
    "Pick one deploy path",
    [
        ("Site", "Choice", "Web messaging", "The path Genesys encourages.", "Messenger snippet"),
        ("Site", "Legacy", "Web chat snippet", "Only if you still run web chat.", "Not inside an iframe"),
        ("Admin", "Tracking", "Digital User Tracking", "On the Messenger configuration.", "Publish the version"),
        ("Admin", "Proof", "Live Now", "Events show up there.", "Then build the action map"),
    ],
    [
        q("Web messaging is deployed with:", "The Messenger snippet", ["Only the legacy tracking snippet", "A BYOC trunk", "An Edge group"], "The tracking-snippet article splits the two paths."),
        q("Where does the legacy tracking snippet go?", "In the head of the main window, not in an iframe", ["In a hidden iframe only", "On the Edge", "In a queue flow"], "The article says not to use an iframe."),
        q("ac('init') belongs to:", "The traditional tracking snippet", ["Messenger Digital User Tracking", "Client credentials", "Bullseye ring 2"], "The SPA snippet uses ac('load') instead."),
        q("Leaving the legacy snippet up after Messenger is deployed:", "Double-tracks the visit", ["Is required", "Disables ACD", "Opens port 5060"], "The migration article says remove it."),
        q("Live Now is how you:", "See that events are arriving", ["Buy a DID", "Set a service level", "Grant the All division"], "The Messenger article names it as the check."),
        q("Action maps that still offer web chat, after you move to messaging, need:", "The action type changed to web messaging", ["A new core region", "A premises Edge", "No change"], "The migration steps include that edit."),
    ],
    [("Messaging", "Messenger snippet."), ("Web chat", "Legacy tracking snippet."), ("One of them", "Remove the snippet when Messenger tracks."), ("Live Now", "Proof that events arrived.")],
    "Write the tag plan",
    ["Messaging or legacy chat.", "Where the snippet sits.", "That the other snippet is absent.", "The Live Now check you will do."],
    "The page has one tracker and a way to see events.",
    ("Double count", "Visitor activity is about twice the web-server page count.", "Both snippets are in the template.", "The migration note says that double-tracks.", "Remove the Predictive Engagement tracking snippet and keep Messenger."),
))

add(lesson(
    "pe-segments", "A segment matches visitors who meet every condition you listed", "Core", 12,
    "At least one condition. More conditions, fewer visitors. Conditions are not shared with the next segment.",
    [
        "The use case describes a segment as a way to categorize visitors by shared behavior and attributes. Attributes it gives as examples include browser, device, location, campaign, and referrer. That list is not a schema. The best-practices page says a segment needs at least one condition, that you should design the conditions for a specific action map, and that adding conditions reduces how many visitors match. Conditions are not shared across segments and outcomes.",
        "The same best-practices page carries the Journey Outcomes deprecation banner. A segment that exists only to feed an outcome trigger is on borrowed time. Build the segment for a visitor you can still recognize from attributes and activity after outcomes stop qualifying action maps.",
    ],
    cites("pe-usecase", "pe-segments", "pe-deprecate"),
    fig("Conditions narrow the segment. They do not copy themselves into the next one.", [
        ("all", "Visitors", "crm", 14, 40),
        ("seg", "Segment", "bot", 48, 40),
        ("map", "Action map", "architect", 82, 40),
    ], [("all", "seg"), ("seg", "map")]),
    "Write conditions you could explain",
    [
        ("Designer", "Purpose", "One action map", "The best-practices page starts there.", "Not a junk drawer"),
        ("Designer", "Condition", "At least one", "Required.", "Attribute or activity"),
        ("Designer", "Narrow", "Each extra condition", "Fewer matches.", "On purpose"),
        ("Designer", "Reuse", "Do not assume sharing", "Conditions stay on that object.", "Copy them if you need them again"),
    ],
    [
        q("A segment with no conditions is:", "Not a defined segment. You need at least one.", ["Matched to everyone by default", "A queue", "A trunk"], "The best-practices page requires a condition."),
        q("Adding conditions generally:", "Matches fewer visitors", ["Matches every visitor", "Raises the service level", "Opens 5061"], "More conditions, fewer matches."),
        q("Conditions are shared automatically with other segments?", "No", ["Yes", "Only on CX 1", "Only for Spanish"], "The page says they are not shared."),
        q("Browser and device are:", "Examples of attributes on the use-case page, not a full list", ["The only legal attributes", "Skills on the agent", "Number-plan types"], "Do not treat the examples as a schema."),
        q("You design segment conditions:", "With a specific action map in mind", ["After the exam", "Inside the SIP URI", "On the Edge group"], "That is the first best practice."),
        q("A segment whose only job is an outcome trigger should be:", "Re-read against the deprecation before you depend on it", ["Copied into a bullseye ring", "Ignored because segments are deprecated", "Turned into a DID"], "Segments remain. Journey Outcomes are the feature on the banner."),
    ],
    [("One condition", "Minimum."), ("More conditions", "Fewer visitors."), ("Not shared", "Copy what you need."), ("Examples", "Not a complete attribute list.")],
    "Draft one segment",
    ["The action map it serves.", "The first condition.", "What a second condition would exclude.", "A note that outcome-only logic needs the deprecation page."],
    "Someone else can see who the segment is for.",
    ("Everyone matches", "A segment with five loose conditions still matches the whole site, and the offer fires constantly.", "The conditions do not describe the audience.", "Each extra real condition narrows the match.", "Replace the loose conditions with ones that name the visitor you meant."),
))

add(lesson(
    "pe-map", "An action map is qualified before it is offered", "Core", 14,
    "Segment, visitor activity, and outcome probability are the trigger kinds. Priority breaks a tie. Web chat is the legacy action.",
    [
        "Creating an action map starts with a name and an action: web messaging, web chat, a content offer, or an advanced orchestration flow. You then set what triggers it. The create page names segment, visitor activity, and outcome. The triggers article is the page that defines those rules, including outcome probability. The overview says a qualified map may still be held back by other offer conditions, and that priority decides which map is offered when several qualify. Web offers can be limited to particular pages.",
        "For a web chat or web messaging offer you can pick an agent queue, and a schedule group so the offer appears only when agents are available. You can override the global frequency cap for one map. The overview’s advice about waiting for a drop in outcome score is tied to Journey Outcomes. Treat that advice as historical design, and read the deprecation before you make outcome probability the only trigger.",
    ],
    cites("pe-create", "pe-triggers", "pe-maps", "pe-actions", "pe-deprecate"),
    fig("Qualified is not the same as shown. Priority and the page still get a vote.", [
        ("t", "Trigger", "bot", 16, 40),
        ("q", "Qualified", "architect", 46, 40),
        ("o", "Offer", "queue", 78, 40),
    ], [("t", "q"), ("q", "o")]),
    "Build the map in that order",
    [
        ("Admin", "Action", "Messaging, chat, content, or flow", "Pick one.", "Messaging is the encouraged chat path"),
        ("Admin", "Trigger", "Segment, activity, or outcome", "The create page lists them.", "Open the triggers article for the rule"),
        ("Admin", "Queue", "Only for chat or messaging", "Optional schedule group.", "Agents available"),
        ("Admin", "Tie", "Priority", "When two maps qualify.", "Page limits still apply"),
    ],
    [
        q("Which of these is an action type on the create page?", "Web messaging, web chat, content offer, or advanced orchestration flow", ["Bullseye ring", "BYOC PBX", "A management unit"], "Those four are the listed actions."),
        q("Priority is used when:", "More than one action map is qualified", ["The trunk is down", "The forecast is long-term", "The grant is implicit"], "The overview says priority picks the offer."),
        q("A schedule group on a messaging offer is for:", "Showing the offer when agents are available", ["Encrypting RTP", "Classifying 911", "Sharing segment conditions"], "The create page names that control."),
        q("Qualified means:", "The trigger matched, and other offer conditions can still stop it", ["The visitor already accepted", "The call is recorded", "The schedule is published"], "The overview separates qualified from offered."),
        q("Outcome probability as the only trigger is:", "A design you re-check against the Journey Outcomes deprecation", ["Required for every map", "The same as a skill", "A firewall port"], "The announcement says outcome triggers stop qualifying after the effective date."),
        q("You can limit a web offer to:", "Specific pages", ["A premises Edge only", "The Home division only", "UDP 5060 only"], "The create and overview pages describe page targeting."),
    ],
    [("Action", "Messaging, chat, content, or flow."), ("Trigger", "Segment, activity, or outcome."), ("Priority", "Chooses among qualified maps."), ("Queue", "Optional, for chat and messaging offers.")],
    "Sketch one map",
    ["Action type.", "Trigger you can explain without an outcome, if you can.", "Queue and schedule, or why there is no queue.", "Priority relative to the other map on that page."],
    "The sketch names an action that still exists if outcomes are removed.",
    ("Offer with nobody there", "The chat offer fires all night and abandons.", "No schedule group. The queue is empty.", "The create page allows a schedule group so the offer waits for agents.", "Add the schedule group or accept the after-hours offer on purpose."),
))

add(lesson(
    "pe-outcomes", "Journey Outcomes have a published end date", "Advanced", 14,
    "Announced 18 May 2026. Planned effective date 29 June 2026. Outcome scoring is not part of the Customer Outcomes replacement.",
    [
        "The deprecation announcement lists the announced date as 2026-05-18 and the planned effective date as 2026-06-29. After that date the page says customers cannot create or manage outcomes, existing outcomes are not processed, new outcome records are not generated, outcomes do not trigger action maps, and outcome reporting is not available. Action maps that have only an outcome trigger stop qualifying. The map is not deleted. The trigger is removed. Architect flows that call getJourneyOutcome skip that branch and otherwise run.",
        "Customer Outcomes is described as a new platform feature under development. It is a simpler event model. The announcement says outcome scoring will not be part of it. A different announcement says a future Predictive Routing framework will take customer-defined business outcomes, including metrics that live outside Genesys Cloud, and that existing predictive-routing configurations need no change until you migrate. This lab read both pages on 15 October 2026, after the planned Journey Outcomes date. It did not sign in to an organization. If either page has moved, the page wins.",
    ],
    cites("pe-deprecate", "pe-kpi", "pe-about"),
    fig("Outcome triggers come off the map. Segment and activity triggers can remain.", [
        ("o", "Outcome", "warn", 22, 62),
        ("m", "Action map", "architect", 55, 30),
        ("s", "Segment", "bot", 84, 62),
    ], [("s", "m")]),
    "Prepare before you promise an outcome score",
    [
        ("Owner", "Inventory", "Maps and flows", "Where outcomes are used.", "The announcement asks for this"),
        ("Owner", "Export", "Reports you still need", "Before they disappear.", "Analytics or the API"),
        ("Owner", "Detach", "Outcome-only triggers", "Those maps stop qualifying.", "Leave a segment or activity trigger if the offer should remain"),
        ("Owner", "Flows", "getJourneyOutcome", "That branch is skipped.", "The rest of the flow runs"),
    ],
    [
        q("The announcement’s planned effective date is:", "2026-06-29", ["2024-01-01", "2027-12-31", "25 May 2026"], "25 May 2026 is the implicit-grant date in the OAuth article, not this one."),
        q("After the effective date, an action map whose only trigger is an outcome:", "Stops qualifying. The map itself is not deleted.", ["Keeps scoring forever", "Deletes the queue", "Becomes a trunk"], "The announcement says the trigger is removed from the configuration."),
        q("getJourneyOutcome after the effective date:", "That branch is skipped and the flow otherwise runs", ["Hangs the call", "Places an emergency call", "Mints a token"], "The announcement describes that skip."),
        q("Customer Outcomes, as described on the deprecation page:", "Is under development and will not include outcome scoring", ["Is already the same screen", "Is a SIP transport", "Replaces Architect"], "Do not promise outcome scores on the new feature."),
        q("The Predictive Routing outcomes announcement says existing routing configs:", "Need no change until you migrate", ["Must be deleted today", "Move to BYOC", "Use implicit grant"], "That sentence is about Predictive Routing, not about keeping Journey Outcomes."),
        q("This lab verified the feature is gone inside a live org?", "No. It read the announcement.", ["Yes", "Only in FedRAMP", "Only for CX 1"], "Re-open the page and look at your own org."),
    ],
    [("Announced", "2026-05-18."), ("Planned end", "2026-06-29."), ("Scoring", "Not in Customer Outcomes."), ("Unverified live", "This lab did not open an org.")],
    "Make a removal list",
    ["Outcome configurations.", "Action maps that trigger only on an outcome.", "Flows that call getJourneyOutcome.", "Reports to export."],
    "Each line has an owner and the announcement is the source.",
    ("Score promise", "A proposal still sells “real-time outcome score” as the reason to buy the website offer.", "The deprecation page says scoring is not part of Customer Outcomes.", "The planned date is already in the past relative to 15 October 2026.", "Rewrite the proposal around segments, activity, and messaging, and quote the announcement."),
    uncertainty="Read on 15 October 2026. The planned effective date on the announcement was 2026-06-29. This lab did not confirm the state of a live organization. Customer Outcomes was still described as under development. The Predictive Routing custom-outcome framework was described as a future release.",
))

add(lesson(
    "pe-flow", "An Architect flow can be the action, and it can also be the thing you must edit", "Advanced", 12,
    "Advanced orchestration is an action type. Flows that still call getJourneyOutcome need a path that does not depend on it.",
    [
        "The about page lists Architect workflows and Architect flow actions as the way to integrate Predictive Engagement with other systems, including a listed topic for Salesforce lead creation and campaign attribution. This lab does not restate Salesforce fields. The create page names advanced orchestration flow as one of the four action types, beside web messaging, web chat, and a content offer.",
        "If that flow asks Journey Outcomes for a score, the deprecation page says the getJourneyOutcome branch is skipped and the flow otherwise runs. Give the visitor a next step that does not need the score: a queue, a content offer, or a segment-based map. The Salesforce topic on the about page is an integration you open in the resource center, not a screen this lab redraws from memory.",
    ],
    cites("pe-about", "pe-create", "pe-deprecate", "architect"),
    fig("The action map calls a flow. The flow still needs a path with no outcome score.", [
        ("m", "Action map", "architect", 18, 40),
        ("f", "Flow", "bot", 50, 40),
        ("q", "Queue", "queue", 82, 40),
    ], [("m", "f"), ("f", "q")]),
    "Give the flow a way out",
    [
        ("Map", "Action", "Advanced orchestration flow", "One of the four types.", "Not a guess"),
        ("Flow", "Work", "Lookup or handoff", "The about page points at Architect actions.", "Do not invent the Salesforce body"),
        ("Flow", "Outcome", "getJourneyOutcome", "Skip that branch after the effective date.", "Do not be the only path"),
        ("Flow", "Exit", "Queue or another offer", "The visitor still has a next step.", "Publish the flow"),
    ],
    [
        q("Advanced orchestration flow is:", "An action type when you create an action map", ["A BYOC trunk subtype", "A forecast view", "A division"], "It sits beside messaging, chat, and content offers."),
        q("This lab’s Salesforce lead steps are:", "Not listed. Open the about page’s integration topic.", ["A copied field map", "The same as the Zendesk embed", "An Edge trunk"], "The about page names the topic. It is not a field list."),
        q("A flow that only succeeds inside getJourneyOutcome:", "Can skip the useful work after the deprecation", ["Is safer", "Ignores the announcement", "Records the card number"], "The announcement says that branch is skipped."),
        q("The rest of the flow, according to the announcement:", "Runs", ["Is deleted", "Becomes a trunk", "Loses its publish"], "Only that branch is skipped."),
        q("The visitor’s fallback should be:", "A queue or another offer that does not need the outcome", ["A second outcome", "Port 80 left open with no owner", "An implicit grant"], "Design the path you will still have."),
        q("You publish the flow because:", "A draft does not run", ["Predictive Engagement publishes it for you", "Live Now publishes it", "The forecast publishes it"], "Architect runtime uses the published version."),
    ],
    [("Four actions", "Messaging, chat, content, flow."), ("No field list", "Open the Salesforce topic."), ("Skipped branch", "getJourneyOutcome."), ("Fallback", "Queue or another offer.")],
    "Mark the outcome branch",
    ["Flow name.", "Whether it calls getJourneyOutcome.", "The fallback action.", "The published version you expect."],
    "The fallback is real and the Salesforce story is a link, not a fiction.",
    ("Dead branch", "Visitors who needed a score now fall out of the flow with no transfer.", "getJourneyOutcome is the only exit.", "That branch is skipped.", "Add a transfer to the queue on the path that remains."),
))

add(lesson(
    "pe-report", "Prove the map with Live Now and the performance reports", "Core", 12,
    "Visitor activity and action-map performance are the Predictive Engagement reports. Outcome columns age out with the deprecation.",
    [
        "The about page points supervisors at live visitor tracking, visitor activity, and action-map performance, and at journey columns on Genesys Cloud performance views. The use case describes visitor activity by device, segments matched, outcomes achieved, and action-map performance for web chat, content offers, and Architect flow. Use those reports to see whether a map fired. Use Live Now when you are still proving that the snippet sees the page.",
        "Outcomes achieved will not stay a trustworthy column through the deprecation. The announcement tells you to export outcome reports you need before the effective date. After that, judge the map by segments, activity, and the offers visitors actually got. A quiet report can mean the snippet is missing, the segment is too narrow, the frequency cap held the offer, or the schedule group hid it because nobody was On Queue.",
    ],
    cites("pe-about", "pe-usecase", "pe-messenger", "pe-deprecate", "pe-create"),
    fig("Live Now proves the tag. The performance report proves the offer.", [
        ("tag", "Snippet", "phone", 14, 40),
        ("now", "Live Now", "wem", 46, 22),
        ("rep", "Reports", "crm", 46, 68),
        ("map", "Action map", "architect", 82, 40),
    ], [("tag", "now"), ("now", "map"), ("map", "rep")]),
    "Separate a dead tag from a quiet map",
    [
        ("Check", "Live Now", "Events or not", "No events means the tag or the domain.", "Not the queue"),
        ("Check", "Segment", "Too many conditions", "Fewer matches.", "Best-practices page"),
        ("Check", "Cap", "Frequency and schedule", "The create page names both.", "A hidden offer is not a failed trunk"),
        ("Check", "Outcomes", "Export, then stop trusting them", "The announcement.", "Use the offer counts that remain"),
    ],
    [
        q("Live Now answers:", "Whether tracking events are arriving", ["Whether the carrier ACL is current", "Whether GC-GCP is expired", "Whether RTP is on 5060"], "It is the tracking check named on the Messenger page."),
        q("Action-map performance, per the use case, covers:", "Web chat, content offers, and Architect flow", ["SIP response codes", "Forecast AHT only", "Edge failover"], "Web messaging is the newer offer type. Confirm its column on the report page."),
        q("A report with no visitors and an empty Live Now view points at:", "Tracking, not ACD", ["Bullseye ring 5", "The wrap-up timeout", "A missing DID"], "The site is not sending events."),
        q("Outcome metrics after the planned effective date should be:", "Exported beforehand and not treated as live", ["The only KPI", "Copied into a number plan", "Used as the emergency route"], "The announcement withdraws outcome reporting."),
        q("A schedule group can make a report look quiet because:", "The offer is withheld when agents are unavailable", ["The snippet doubles", "The core region moved", "TLS was set to UDP"], "That control is on the create page."),
        q("Device type belongs in:", "The visitor activity view described on the use case", ["The trunk transport", "The OAuth basic header", "The Home division name"], "The use case names a device drill-down."),
    ],
    [("Live Now", "Events are arriving."), ("Activity", "Devices, segments."), ("Map report", "Did the offer run."), ("Outcomes", "Export, then let them go.")],
    "Write the quiet-report checks",
    ["Live Now, yes or no.", "Segment conditions.", "Frequency cap and schedule group.", "Whether the column you miss is an outcome metric."],
    "The first failed check is the one you fix.",
    ("Wrong system", "The website team opens a telephony ticket because action-map performance is empty.", "Live Now is also empty. The queue is taking inbound calls.", "Tracking never started.", "Fix the Messenger deployment before you touch the trunk."),
    uncertainty="The use case names action types web chat, content offers, and Architect flow. It does not, in the section this lab used, name a web-messaging column. Confirm that column on the report before you tell someone it is missing.",
))
