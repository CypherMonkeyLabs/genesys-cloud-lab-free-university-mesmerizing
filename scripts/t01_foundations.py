from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "foundations",
    "title": "Foundations",
    "kicker": "Start here",
    "accent": 1,
    "summary": "What Genesys Cloud CX is, where an organization lives, and how a voice conversation is supposed to move.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "f-platform", "What Genesys Cloud CX is", "Foundation", 14,
    "Genesys Cloud CX is a subscription contact-center platform with four nested packages, not a single feature switch.",
    [
        "The overview article names four packages. Genesys Cloud CX 1 is the voice package: inbound and outbound voice, secure IVR, callbacks, and voice campaigns. CX 2 adds the digital channels and the quality and compliance layer on top of CX 1. CX 3 adds workforce engagement management and voice transcription minutes. CX 4 adds Agent Copilot, Journey Management, and a published AI token allotment: 30 tokens for a named user and 39 for a concurrent user.",
        "Each higher package includes the lower ones. A design that needs scheduling and transcription is a CX 3 conversation. A design that needs Agent Copilot is a CX 4 conversation. The December 2023 feature-matrix PDF is a historical summary and does not describe CX 4 the way the current overview does.",
    ],
    cites("overview", "copilot"),
    fig("CX packages stack from voice to AI.", [
        ("cx1", "CX 1 voice", "phone", 12, 70),
        ("cx2", "CX 2 digital", "queue", 36, 50),
        ("cx3", "CX 3 WEM", "wem", 62, 32),
        ("cx4", "CX 4 AI", "bot", 84, 16),
    ], [("cx1", "cx2"), ("cx2", "cx3"), ("cx3", "cx4")]),
    "How a buyer reads the package stack",
    [
        ("Buyer", "Overview", "CX 1", "Voice, secure IVR, callbacks, campaigns.", "Package: Genesys Cloud CX 1"),
        ("Buyer", "Overview", "CX 2", "Adds digital channels and quality.", "Includes CX 1"),
        ("Buyer", "Overview", "CX 3", "Adds WEM and transcription minutes.", "Includes CX 1 and CX 2"),
        ("Buyer", "Overview", "CX 4", "Adds Agent Copilot, Journey Management, tokens.", "30 named / 39 concurrent tokens"),
        ("Buyer", "Resource Center", "Check the page", "The live overview wins over an old matrix PDF.", "PDF date in the lab notes: 2023-12-06"),
    ],
    [
        q("Which package first includes workforce engagement management?", "Genesys Cloud CX 3", ["Genesys Cloud CX 1", "Genesys Cloud CX 2", "A free developer org"], "The overview lists WEM on CX 3, which also includes CX 1 and CX 2."),
        q("What does the overview add at CX 4 beyond CX 3?", "Agent Copilot, Journey Management, and AI tokens", ["A second AWS region for free", "On-premises ICM", "Unlimited SIP trunks"], "Those three items are the CX 4 additions named on the overview."),
        q("How many AI tokens does the overview list for a named CX 4 user?", "30", ["5", "39", "100"], "39 is the concurrent figure. 30 is the named figure."),
        q("CX 2 is best described as which of these?", "CX 1 plus digital channels and quality", ["A voice-only bundle", "WEM without voice", "A PureConnect license"], "The overview builds each package on the previous one."),
        q("Why is the 2023 feature-matrix PDF a weak source for CX 4?", "It predates the CX 4 description on the current overview", ["Genesys removed CX 1", "PDFs cannot describe voice", "CX 4 is only a community nickname"], "Use the overview article for the current package story."),
        q("Secure IVR and voice campaigns are introduced at which package?", "Genesys Cloud CX 1", ["CX 4 only", "CX 3 only", "AppFoundry only"], "The overview places them in the voice package."),
    ],
    [
        ("CX 1", "Voice package: inbound and outbound voice, secure IVR, callbacks, campaigns."),
        ("CX 3", "Adds WEM and voice transcription minutes on top of CX 1 and CX 2."),
        ("CX 4 tokens", "30 named, 39 concurrent, as published on the overview."),
        ("Old matrix", "A dated PDF is not the source for the current CX 4 description."),
    ],
    "Read the package you actually own",
    ["Open the overview article and write down what CX 1, CX 2, CX 3, and CX 4 each add.", "Circle the first package that includes WEM.", "Find the named and concurrent token numbers for CX 4.", "Note that a 2023 matrix is historical."],
    "You can say which package a design requires without guessing.",
    ("Package mismatch", "Agents expect schedules, but the org only shows voice queues.", "License view: Genesys Cloud CX 1 assigned. WFM admin pages are absent.", "WEM is a CX 3 capability in the overview, not a CX 1 feature.", "Move the users who need scheduling to a package that includes CX 3, or drop the WFM scope."),
))

add(lesson(
    "f-regions", "Core regions and satellite media", "Foundation", 16,
    "An organization is born in one core AWS region. Satellite regions carry media. They do not host the org.",
    [
        "When an organization is created, Genesys Cloud deploys it in a core region and sends users to that region’s login URL. US East (N. Virginia, us-east-1) uses https://login.mypurecloud.com. US West (Oregon, us-west-2) uses https://login.usw2.pure.cloud. The FedRAMP region (US East 2, Ohio, us-east-2) uses https://login.use2.us-gov-pure.cloud. The regions article is the full table. Do not invent a login host for a row you have not opened.",
        "Satellite regions exist for Global Media Fabric. They add places for call and audio paths, including recording storage, so media does not have to hairpin to the core. A satellite region cannot be the AWS region where the organization itself is deployed. Some core regions offer Genesys Cloud Voice and some do not. Voice coverage, including which countries can buy numbers, is a separate article from the org-deployment list.",
    ],
    cites("regions", "gcv-regions"),
    fig("Core region holds the org. Satellite regions shorten media.", [
        ("org", "Core org", "region", 30, 40),
        ("sat", "Satellite media", "trunk", 68, 28),
        ("rec", "Recording", "wem", 68, 68),
    ], [("org", "sat"), ("sat", "rec")]),
    "Where a new org actually lands",
    [
        ("Admin", "Core region", "Create org", "The org is placed in one core region.", "Login URL follows that row"),
        ("User", "Login host", "Sign in", "US East uses login.mypurecloud.com.", "us-east-1"),
        ("Media", "Satellite", "Audio path", "Global Media Fabric can anchor media closer to the site.", "Satellite is not an org home"),
        ("Buyer", "GCV table", "Voice check", "Number and calling coverage is its own article.", "FedRAMP voice is US-only in that article"),
        ("Engineer", "Regions page", "Confirm", "Read the row before you hardcode a host.", "Do not copy a host from memory"),
    ],
    [
        q("Can a satellite region be the deployment region for an organization?", "No. A satellite region cannot host the org.", ["Yes, for orgs under 50 users", "Yes, if you buy CX 4", "Only on Tuesdays"], "The regions article says a satellite cannot act as the deployment region."),
        q("Which login URL does the regions article list for Americas (US East)?", "https://login.mypurecloud.com", ["https://login.usw2.pure.cloud", "https://login.use2.us-gov-pure.cloud", "https://api.genesys.com"], "US East is us-east-1 and that login host."),
        q("What is a satellite region for?", "Extra media locations, including recording storage, via Global Media Fabric", ["A second billing org", "A PureConnect core", "An AppFoundry tenant"], "Satellites shorten media paths. They are not a second organization."),
        q("US West (Oregon) maps to which AWS region name in the article?", "us-west-2", ["us-east-1", "eu-west-1", "af-south-1"], "The article pairs US West (Oregon) with us-west-2."),
        q("Where do you confirm Genesys Cloud Voice country coverage?", "The Genesys Cloud Voice regions article, not the org-deployment table alone", ["Any RFC", "The Architect home page", "A queue name"], "Voice availability is documented separately and has country restrictions."),
        q("FedRAMP in the regions table is which AWS region?", "US East 2 (Ohio), us-east-2", ["US West", "Ireland", "São Paulo"], "The article lists the FedRAMP login on us-east-2."),
    ],
    [
        ("Core vs satellite", "Core hosts the org. Satellite hosts media paths and cannot be the org region."),
        ("US East login", "https://login.mypurecloud.com for us-east-1."),
        ("US West login", "https://login.usw2.pure.cloud for us-west-2."),
        ("Voice coverage", "Read the Genesys Cloud Voice region article before you promise numbers."),
    ],
    "Pin an org to its region row",
    ["Open the AWS regions article.", "Find the login URL for the region you think you are in.", "Find one satellite region and write why it cannot hold the org.", "Open the Genesys Cloud Voice region article and note one restriction."],
    "You can point at the right login host and you know where voice coverage is documented.",
    ("Wrong login host", "A script gets a token from login.mypurecloud.com and then sees none of the production users.", "Org home region: Americas (US West). Token request host: login.mypurecloud.com.", "US West users authenticate at login.usw2.pure.cloud. The US East host is a different core.", "Retarget the OAuth client and the API host to the org’s documented region row."),
    "Other core regions exist on the same article, including Canada, Ireland, Frankfurt, London, Tokyo, and more. This lesson only hardcodes the three login URLs quoted from the table in full.",
))

add(lesson(
    "f-sip", "SIP, RTP, and what the trunk is doing", "Foundation", 15,
    "SIP sets the call up. RTP moves the audio. They are different protocols, and Genesys trunks speak both.",
    [
        "RFC 3261 is the Session Initiation Protocol. An INVITE offers a session, responses such as 100, 180, and 200 move the dialog along, and ACK confirms the 200. The media description inside that signaling is not the audio itself. RFC 3550 is RTP, the stream of audio packets. RFC 3711 is SRTP, the encrypted form of that stream. RFC 4733 is how telephone events such as DTMF digits can ride in the RTP stream instead of in the audio band.",
        "BYOC Cloud places a SIP trunk between the Genesys Cloud media tier in AWS and a carrier or PBX that has a public address. The audio is RTP across the internet, so latency and loss on that path are part of the design. Example addresses in this lab use the documentation ranges in RFC 5737, such as 192.0.2.10, and are not a customer capture.",
    ],
    cites("rfc3261", "rfc3550", "rfc3711", "rfc4733", "byoc-overview", "rfc5737"),
    fig("Signaling and media take different paths.", [
        ("carrier", "Carrier", "carrier", 12, 40),
        ("sip", "SIP", "trunk", 40, 22),
        ("rtp", "RTP", "phone", 40, 70),
        ("media", "Media tier", "region", 78, 40),
    ], [("carrier", "sip"), ("sip", "media"), ("carrier", "rtp"), ("rtp", "media")]),
    "A lab INVITE, not a capture",
    [
        ("Carrier", "BYOC trunk", "INVITE", "The carrier offers a session toward a public trunk address.", "INVITE sip:+15555550100@192.0.2.10 SIP/2.0"),
        ("BYOC trunk", "Carrier", "100 Trying", "The trunk accepted the INVITE into processing.", "SIP/2.0 100 Trying"),
        ("BYOC trunk", "Carrier", "180 Ringing", "Alerting has started. Audio is still not a conversation.", "SIP/2.0 180 Ringing"),
        ("Media", "Media", "RTP", "RFC 3550 packets carry the voice once the session is up.", "UDP media, not the SIP dialog"),
        ("Phone", "Media", "DTMF", "A digit can be an RFC 4733 telephone event.", "Payload telephone-event"),
    ],
    [
        q("Which RFC defines SIP?", "RFC 3261", ["RFC 3550", "RFC 3711", "RFC 5737"], "3261 is SIP. 3550 is RTP. 3711 is SRTP. 5737 is documentation addresses."),
        q("What does RTP carry that SIP does not?", "The media packets of the conversation", ["The queue membership list", "OAuth tokens", "Division IDs"], "SIP sets up the session. RTP moves the audio."),
        q("SRTP is specified in which RFC?", "RFC 3711", ["RFC 4733", "RFC 3261", "RFC 3550"], "3711 is Secure RTP."),
        q("Why does this lab use 192.0.2.10 in sample messages?", "RFC 5737 reserves it for documentation", ["It is a Genesys anycast address", "It is the US East login host", "It is a customer SBC"], "Documentation ranges must not be mistaken for a live capture."),
        q("BYOC Cloud media between AWS and the carrier is which protocol family?", "RTP over the internet", ["An Architect expression", "SCIM", "A screen recording"], "The BYOC Cloud overview calls out RTP across the public internet."),
        q("RFC 4733 is the right citation for which event?", "DTMF telephone events in RTP", ["OAuth client credentials", "Bullseye ring timers", "Queue member limits"], "4733 covers telephone events such as digits."),
    ],
    [
        ("SIP", "RFC 3261. Session setup, not the audio packets."),
        ("RTP", "RFC 3550. The audio stream."),
        ("SRTP", "RFC 3711. Encrypted RTP."),
        ("DTMF", "RFC 4733 telephone events, when digits must not depend on in-band audio."),
    ],
    "Label a sample INVITE",
    ["Write a one-line INVITE that uses 192.0.2.10.", "Name the RFC that makes that address safe for a lab.", "Point at which line would be SIP and which path would be RTP.", "Name the RFC you would cite for a DTMF digit."],
    "You can separate signaling from media without inventing headers.",
    ("One-way audio", "The caller hears ringing, then silence, while the agent hears the caller.", "SIP: 200 OK and ACK both completed. RTP from 192.0.2.11 toward the media tier: zero packets for 8 seconds.", "The dialog is up. The RTP path is not. Signaling success does not prove media.", "Inspect firewall and NAT for the UDP media range with the carrier, using the BYOC port guidance, before you rewrite the Architect flow."),
))

add(lesson(
    "f-acd-idea", "What ACD is before you name a queue", "Foundation", 12,
    "ACD picks an agent for a waiting interaction. The queue is the waiting line. Skills, utilization, and On Queue decide who is eligible.",
    [
        "Genesys Cloud queues are the waiting lines. An agent enters the queues they belong to by choosing On Queue. A queue name is unique, cannot contain special characters, and can hold at most 5,000 members. The queue also belongs to a division, which is how access control reaches it.",
        "Routing methods decide how that waiting line offers work: standard, predictive, bullseye, preferred agent, and conditional group routing. Evaluation methods decide what “has the skills” means. Utilization decides whether an agent who is already busy may take another interaction. Those controls are the rest of this lab. This lesson only fixes the vocabulary.",
    ],
    cites("queues", "routing", "util"),
    fig("A queue offers work only to agents who are On Queue.", [
        ("in", "Interaction", "phone", 12, 40),
        ("q", "Queue", "queue", 42, 40),
        ("on", "On Queue", "agent", 72, 22),
        ("off", "Off queue", "agent", 72, 70),
    ], [("in", "q"), ("q", "on")]),
    "From arrival to an eligible agent",
    [
        ("Caller", "Queue", "Enqueue", "The interaction waits on a named queue.", "Queue name is unique"),
        ("Agent", "Workspace", "On Queue", "Only On Queue agents are candidates.", "Off-queue agents are invisible to ACD"),
        ("ACD", "Profile", "Skills", "The evaluation method decides if skills are required.", "All, best, or disregard"),
        ("ACD", "Utilization", "Capacity", "A full agent is skipped.", "Defaults include one voice call"),
        ("ACD", "Agent", "Alert", "Voice alerting is 7 to 59 seconds.", "Then Not Responding"),
    ],
    [
        q("What is the documented member cap on one queue?", "5000", ["50", "500", "Unlimited"], "Create and configure queues states the 5,000 member limit."),
        q("Which status puts an agent into the queues they belong to?", "On Queue", ["Available", "Busy", "Meeting"], "The queue article says agents select On Queue."),
        q("A queue name may not contain which of these?", "Special characters", ["Letters", "Digits", "A division"], "Names must be unique and free of special characters."),
        q("Which routing method is the default named in the routing settings article?", "Standard routing", ["Predictive routing", "Bullseye routing", "Preferred agent routing"], "Standard is the documented default."),
        q("Utilization is best described as which control?", "How many interactions of each media an agent may hold", ["The SIP response code", "The login region", "The OAuth grant"], "The utilization article defines per-media capacity."),
        q("Voice alerting timeout must fall in which documented range?", "7 to 59 seconds", ["1 to 3 seconds", "2 seconds to 72 hours", "Exactly 30 seconds"], "7 to 59 is the alerting range. The 72 hour figure belongs to other timers."),
    ],
    [
        ("Queue", "The waiting line. Unique name, no special characters, 5,000 members."),
        ("On Queue", "The status that makes an agent eligible for ACD work."),
        ("Routing method", "Standard, predictive, bullseye, preferred, or conditional group."),
        ("Alerting", "7 to 59 seconds on voice, then Not Responding."),
    ],
    "Say the five routing methods out loud",
    ["List standard, predictive, bullseye, preferred agent, and conditional group routing.", "State the queue member cap.", "State the voice alerting range.", "Explain On Queue in one sentence."],
    "You can brief a new admin without mixing timers from different features.",
    ("Ghost queue", "Agents are logged in and idle, and the queue stays at zero answered.", "Presence: Available. Routing status: Off Queue. Queue membership: Billing voice.", "Available is not On Queue. ACD does not offer the interaction.", "Have the agent select On Queue, then confirm membership on that queue."),
))

add(lesson(
    "f-digital", "Digital conversations beside voice", "Foundation", 12,
    "Voice is one media. Architect also has inbound message, email, and chat flows, and queues track those medias separately.",
    [
        "The Architect home page lists inbound message, inbound email, and inbound chat alongside inbound call. In-queue flows exist for calls, email, and messages. Call flows ship with a default in-queue flow that is not published until you publish it. Email and message queues do not get that built-in default. You create those in-queue flows yourself.",
        "Utilization counts medias separately. The documented defaults are one voice call, one email, one callback, up to four chats, up to four messages, and up to four workitems. A designer who copies a voice queue and expects the same in-queue music on email has skipped the flow-type list.",
    ],
    cites("arch-home", "inqueue", "util"),
    fig("Voice and digital flows are different Architect types.", [
        ("call", "Inbound call", "phone", 16, 30),
        ("msg", "Message", "queue", 42, 30),
        ("mail", "Email", "crm", 68, 30),
        ("iq", "In-queue", "architect", 42, 72),
    ], [("call", "iq"), ("msg", "iq"), ("mail", "iq")]),
    "Pick the flow type before the prompt",
    [
        ("Admin", "Architect", "Open Flows", "The home page is a list of flow types.", "Call, message, email, chat"),
        ("Admin", "In-queue call", "Default", "A default call in-queue flow exists and still needs a publish.", "Unpublished means unused"),
        ("Admin", "In-queue email", "Create", "Email has no built-in default in-queue flow.", "Create one on the queue"),
        ("ACD", "Utilization", "Media caps", "Chats and messages default higher than voice.", "4 chats, 1 call"),
        ("Agent", "Workspace", "Handle", "The agent can hold mixed medias up to those caps.", "Interrupt rules are separate"),
    ],
    [
        q("Does Architect publish the default in-queue call flow for you?", "No. You must publish it before it handles waiting calls.", ["Yes, on org creation", "Only for email", "Only in FedRAMP"], "The in-queue overview says the default is not automatically published."),
        q("Email and message in-queue flows differ from calls because:", "There is no built-in default. You create them.", ["They cannot transfer to a queue", "They ignore divisions", "They use RTP"], "The overview says Architect does not include a built-in default for email and message."),
        q("Default chat utilization is up to how many?", "4", ["1", "2", "10"], "The utilization article lists up to four chats."),
        q("Default voice utilization is how many calls?", "1", ["4", "8", "0"], "One voice call is the documented default."),
        q("Which Architect home tab is the right place for a WhatsApp-style inbound message?", "Inbound message", ["Inbound call", "Secure call", "Workflow only"], "Inbound message is the documented flow type for ACD messages."),
        q("Workitems appear in which default utilization row?", "Up to four", ["They are not an interaction type", "Unlimited", "One per week"], "The utilization summary includes up to four workitems."),
    ],
    [
        ("In-queue call", "A default exists. It does nothing until you publish it."),
        ("In-queue email", "No built-in default. Create the flow."),
        ("Default voice cap", "One call."),
        ("Default message cap", "Up to four messages."),
    ],
    "Match media to a flow type",
    ["Name the Architect flow type for a phone call, an email, and a message.", "State whether each has a built-in in-queue flow.", "Write the default utilization for calls and for chats.", "Explain why publishing matters."],
    "You can tell a voice design from a digital design before you draw the flow.",
    ("Silent hold", "Voice callers sit in silence. The queue is staffed.", "In-queue flow: Default In-Queue. Published: no.", "The built-in flow is not live until it is published.", "Publish the in-queue call flow, or assign a published one on the queue."),
))

add(lesson(
    "f-access", "Divisions, before roles get complicated", "Foundation", 13,
    "A division groups objects inside one organization. It is not a second org, and the Home division cannot be deleted.",
    [
        "Administrators group configuration objects into divisions and then grant roles against those divisions. A queue lives in one division. Users reach objects by holding a role in the division that contains them. Every organization has a Home division. You can move objects into and out of Home. You cannot delete Home.",
        "Until you create more divisions, new configuration objects land in a way the article describes through the All division concept: All grants organization-wide access, and transactional objects such as conversations, recordings, presence history, and audit data pick up division associations as they move. You move an object between divisions. You do not add a second division membership to the same queue.",
    ],
    cites("divisions"),
    fig("One org, many divisions, one home you cannot delete.", [
        ("org", "Organization", "region", 18, 30),
        ("home", "Home", "queue", 48, 22),
        ("emea", "EMEA", "queue", 48, 70),
        ("role", "Role", "agent", 80, 40),
    ], [("org", "home"), ("org", "emea"), ("role", "emea")]),
    "Move a queue, do not clone the org",
    [
        ("Admin", "Home", "See default", "Home exists in every org and cannot be deleted.", "Objects can move"),
        ("Admin", "New division", "Create EMEA", "A division groups objects. It is still one org.", "Not a new region"),
        ("Admin", "Queue", "Move", "The queue leaves its old division.", "One division at a time"),
        ("Admin", "Role", "Grant", "The role is paired with the division.", "No division, no objects"),
        ("Conversation", "Division", "Transactional", "The live conversation picks up division context as it travels.", "Recordings included"),
    ],
    [
        q("Can you delete the Home division?", "No", ["Yes, after the last queue leaves", "Yes, on CX 4", "Only the All division is permanent"], "The divisions article says Home cannot be deleted."),
        q("A division is which of these?", "A grouping of objects inside one organization", ["A separate AWS region", "A SIP trunk", "An OAuth grant"], "Divisions segregate objects without a second org."),
        q("How does a queue change division?", "You move it. It belongs to one division.", ["You add it to every division", "You rename the org", "You publish an Architect flow"], "Objects are moved, not multi-homed."),
        q("Which list is called out as transactional objects?", "Conversations, recordings, presence history, and audit data", ["SIP trunks only", "Number plans only", "OAuth secrets"], "The divisions article names those transactional objects."),
        q("All division is best described as:", "Organization-wide access until you split objects up", ["The FedRAMP region", "A queue of 5,000 bots", "The default in-queue flow"], "All is the org-wide access concept in the same article."),
        q("Users see a division’s objects when:", "Their role is granted on that division", ["They know the queue name", "They place one outbound call", "They open Architect"], "Roles are how division access is granted."),
    ],
    [
        ("Home", "Always present. Cannot be deleted. Objects can move."),
        ("Move, not copy", "A queue belongs to one division."),
        ("Role + division", "That pair is what lets a user see the objects."),
        ("Transactional", "Conversations and recordings carry division context too."),
    ],
    "Draw your org as divisions",
    ["Name the division that must exist.", "Pick two business units that deserve their own division.", "Write which objects you would move.", "Write which role would be granted on each."],
    "You can explain Home versus a new division without creating a second org.",
    ("Invisible queue", "An EMEA supervisor cannot see the EMEA queue.", "Queue division: EMEA. Supervisor roles: Home only.", "The role is not granted on the division that holds the queue.", "Grant the supervisor role on EMEA, or move the queue into a division they already have."),
))

add(lesson(
    "f-read", "How to read a Genesys page without inventing the rest", "Foundation", 11,
    "This lab cites the Resource Center, the Developer Center, Genesys Education, and RFCs. The page wins when they differ.",
    [
        "Implementation facts in this lab were checked against public pages on 14 October 2026. Certifications are the names on the Genesys Education cloud exam catalog, including GC-GCP and GC-GCD in the catalog header. Specialist rows are named there without this lab inventing extra exam codes. Community threads still say GCX- in places. Treat the catalog as the current list.",
        "The Developer Center’s client-credentials guide is the source for the token request, not a blog. The Resource Center is the source for admin behavior. When a summary on a help page and a sentence lower on the same page disagree, read the procedure, not only the generated summary. Fair-use numbers change. This lab points at the policy instead of copying the rate card.",
    ],
    cites("certs", "cert-note", "cc-grant", "fair"),
    fig("Four places a citation is allowed to point.", [
        ("rc", "Resource Center", "region", 18, 30),
        ("dev", "Developer Center", "trunk", 42, 30),
        ("edu", "Education", "wem", 66, 30),
        ("rfc", "RFC", "phone", 84, 70),
    ], [("rc", "dev"), ("edu", "rfc")]),
    "Check a claim before you repeat it",
    [
        ("You", "Catalog", "Open exams", "Read the certification name on the education page.", "GC-GCP and GC-GCD are in the header"),
        ("You", "Article", "Open the procedure", "Prefer the numbered steps over a one-line summary.", "Summaries can compress"),
        ("You", "API guide", "Read the grant", "Client credentials are not a user.", "/users/me is called out"),
        ("You", "Fair use", "Do not memorize rates", "The policy page holds the current table.", "Rates change"),
        ("You", "Lab", "Mark uncertainty", "If the lab says confirm, open the link.", "The page wins"),
    ],
    [
        q("Which catalog codes does the Genesys Education cloud page put in the header?", "GC-GCP and GC-GCD", ["GCX-ARC and GCX-WFM", "CCNA and CCIE", "MS-721"], "The fetched catalog header uses GC-GCP and GC-GCD. This lab does not invent specialist codes."),
        q("A client-credentials token is documented as which kind of caller?", "A non-user application", ["The logged-in agent", "A division", "A queue"], "The grant is for headless apps and cannot call user-context APIs such as /api/v2/users/me."),
        q("Where should a rate-card number come from?", "The current fair use policy page", ["This lab’s memory", "A 2023 PDF only", "An RFC"], "The policy is the rate source, and it changes."),
        q("What should you do when this lab and a vendor page disagree?", "Trust the vendor page", ["Trust the lab", "Average them", "Trust a forum dump site"], "The lab is a study guide with links, not the product."),
        q("Why does the lab avoid GCX- exam codes?", "The current catalog header shows GC-GCP and GC-GCD, and specialist codes are not invented here", ["Genesys has no exams", "GCX is a SIP method", "The codes were never used in community posts"], "Older posts use GCX-. The catalog is the source this lab follows."),
        q("Which announcement is safe to repeat from the education notice?", "Speech and Text Analytics certification is open, and practice exams exist", ["All exams were retired in 2024", "Architect is the only remaining exam", "Webcam rules end in 2024"], "The announcement page says STA is open and describes free practice exams."),
    ],
    [
        ("Catalog header", "GC-GCP professional, GC-GCD developer."),
        ("Do not invent codes", "Specialist names are cited. Extra codes are not."),
        ("Client credentials", "Not a user. /api/v2/users/me is out of scope for that token."),
        ("Fair use", "Link the policy. Do not freeze a price in a lesson."),
    ],
    "Open three primary sources",
    ["Open the cloud certification catalog and write the two header codes.", "Open the client-credentials guide and find the sentence about /users/me.", "Open the fair use policy and notice that it is a table, not a slogan."],
    "You know which site owns which kind of fact.",
    ("Stale code in a study sheet", "A candidate searches for GCX-GCP and finds conflicting names.", "Catalog header: Genesys Cloud: Professional Certification (GC-GCP).", "The public catalog and older forum posts use different prefixes.", "Study the catalog name and the linked preparation courses, and treat other prefixes as historical unless the course page prints them."),
    "The education announcement also says external webcam rules for online proctoring are relaxed until 31 December 2026, practice exams are 25 to 30 questions and do not need a voucher, and Japanese exams are available except Architect. Re-read that notice before you book.",
))

add(lesson(
    "f-prereq", "Prerequisites before the first trunk", "Foundation", 13,
    "BYOC Cloud needs a public carrier address, an open port plan, and a real location. The org subscription has to include the telephony product you intend to use.",
    [
        "The BYOC Cloud quick start assumes the organization exists and the BYOC Cloud product is on the subscription. You then work the carrier requirements, add a physical location, create a BYOC Carrier or BYOC PBX trunk, attach that trunk to an outbound route, and add number plans as needed. The location is not cosmetic. Emergency calling with BYOC uses it, and Genesys warns that it is not responsible for emergency calls that ride a BYOC trunk.",
        "New BYOC Cloud trunks should use the Dynamic Cloud Voice platform. RTP still crosses the internet, so you judge latency before you promise a voice quality number you have not measured. Monitoring cloud media resources is the documented place to look at that cloud media, not a packet capture from a laptop as the only tool.",
    ],
    cites("byoc-quick", "byoc-overview", "emergency", "dcvp", "media-mon"),
    fig("Quick start order for a BYOC Cloud trunk.", [
        ("org", "Org", "region", 10, 40),
        ("loc", "Location", "phone", 30, 40),
        ("trunk", "Trunk", "trunk", 52, 40),
        ("route", "Route", "queue", 74, 40),
        ("plan", "Number plan", "architect", 90, 70),
    ], [("org", "loc"), ("loc", "trunk"), ("trunk", "route"), ("route", "plan")]),
    "Stand up a trunk in the documented order",
    [
        ("Admin", "Subscription", "Confirm BYOC", "The quick start assumes the product is on the subscription.", "Org already exists"),
        ("Admin", "Location", "Add a place", "Emergency and the site need a physical location.", "Not a postal fiction"),
        ("Admin", "Trunk", "Carrier or PBX", "Two BYOC Cloud trunk types.", "Public address required"),
        ("Admin", "DCVP", "New trunks", "New trunks should use Dynamic Cloud Voice.", "Test before production"),
        ("Admin", "Route", "Assign trunk", "An outbound route needs the trunk.", "Number plan classifies"),
    ],
    [
        q("What does the BYOC quick start assume is already true?", "The org exists and BYOC Cloud is on the subscription", ["A premises Edge is installed", "CX 4 tokens are loaded", "A PureConnect handler is exported"], "Those two prerequisites open the guide."),
        q("Why does the quick start send you to Add Locations early?", "The site needs a physical location, including for emergency services", ["Locations replace queues", "Locations are SIP methods", "Locations set the OAuth grant"], "The guide ties location to enabling services and to emergency."),
        q("New BYOC Cloud trunks should use which platform?", "Dynamic Cloud Voice", ["The original platform only", "A hardware Edge only", "WebRTC with no trunk"], "The quick start points new trunks at Dynamic Cloud Voice."),
        q("Genesys’ own warning on BYOC emergency calls is:", "Genesys is not responsible when emergency calls use BYOC trunks", ["Genesys answers 911 as the PSAP", "Emergency is blocked on all trunks", "Emergency ignores locations"], "The emergency article states that warning directly."),
        q("BYOC Cloud requires the far end to have:", "A publicly reachable address and open ports", ["A private RFC 1918 address only", "An Architect bot", "A WFM business unit"], "The overview requires a public address and the right ports."),
        q("Where does Genesys tell you to watch cloud media?", "Monitor cloud media resources", ["The fair use rate card", "The certification catalog", "RFC 3261"], "That article is the documented monitoring page."),
    ],
    [
        ("Order", "Location, trunk, outbound route, number plan."),
        ("DCVP", "Use it for new BYOC Cloud trunks."),
        ("Public address", "The carrier or PBX must be reachable."),
        ("Emergency warning", "BYOC emergency is your carrier’s service, not Genesys’."),
    ],
    "Write the quick-start checklist",
    ["List the four configuration objects in order.", "Write the Dynamic Cloud Voice requirement in your own words.", "Write the emergency warning in your own words.", "Name the monitoring article."],
    "You can brief a carrier turn-up without skipping the location.",
    ("Trunk with no route", "Inbound numbers work. Outbound dialing finds no trunk.", "External trunk: Carrier-A, in service. Outbound route: default, trunk assignment empty.", "The quick start says Genesys creates default outbound routes and you still must assign a trunk.", "Assign Carrier-A on the outbound route for the classifications you dial."),
))

# silence unused import if any
_ = cites
