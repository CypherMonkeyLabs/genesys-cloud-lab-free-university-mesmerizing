"""Glossary, certifications, boss incidents, and interview drills.

Facts point at pages already used in the tracks. Synthetic logs use RFC 5737
documentation addresses and fictional 555 numbers.
"""

CATALOG = "https://education.genesys.com/certification/cloud"
ANNOUNCE = "https://education.genesys.com/explore/announcement/genesys-technical-certifications-important-announcement"

REFERENCE = {
    "certNote": "Read on 14 October 2026 from the Genesys Cloud exams catalog and the technical certifications announcement. GC-GCP and GC-GCD are the catalog codes named there. Specialist and AI rows are given by name and course number, not by a GCX- prefix. The announcement describes an external-webcam relaxation through 31 December 2026 and free practice exams of about 25 to 30 questions that do not include a voucher. Re-open both pages before you enroll or book. Engage on-premises exams are a separate catalog section.",
    "certs": [
        {
            "name": "Genesys Cloud Professional Certification (GC-GCP)",
            "detail": "One exam. The catalog lists prep courses Implementation (135), Contact Center Administration (140), and Reporting and Analytics (143). Cert course 17089.",
            "url": CATALOG,
        },
        {
            "name": "Genesys Cloud Developer Certification (GC-GCD)",
            "detail": "One exam. Prep is the API course 11874. Cert course 17173.",
            "url": CATALOG,
        },
        {
            "name": "Architect specialist",
            "detail": "Named specialist row. Cert course 11975. Prep Architect course 660. This lab does not assign a GCX- code.",
            "url": CATALOG,
        },
        {
            "name": "Workforce Management specialist",
            "detail": "Named specialist row. Cert course 12173. Prep WEM–Workforce Management course 11304.",
            "url": CATALOG,
        },
        {
            "name": "Scripting specialist",
            "detail": "Named specialist row. Cert course 12174. Prep Designing and Managing Scripts course 11551.",
            "url": CATALOG,
        },
        {
            "name": "Quality Management specialist",
            "detail": "Named specialist row. Cert course 12175. Prep course 11872.",
            "url": CATALOG,
        },
        {
            "name": "Outbound specialist",
            "detail": "Named specialist row. Cert course 16125. Prep course 11550.",
            "url": CATALOG,
        },
        {
            "name": "Speech and Text Analytics specialist",
            "detail": "Named specialist row. Cert course 18415. Prep course 18412. Separate from the AI exams.",
            "url": CATALOG,
        },
        {
            "name": "AI – GPE & GPR",
            "detail": "One exam. Catalog course 17671.",
            "url": CATALOG,
        },
        {
            "name": "AI – Digital Bots & Knowledge",
            "detail": "One exam. Catalog course 18174. Not the same row as GPE & GPR.",
            "url": CATALOG,
        },
    ],
    "glossary": [
        {"term": "Core region", "def": "The AWS region where the organization is created. Users sign in on that region’s login host.", "url": "https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/", "source": "AWS regions"},
        {"term": "Satellite region", "def": "A Global Media Fabric place for media. It cannot host the organization.", "url": "https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/", "source": "AWS regions"},
        {"term": "Division", "def": "A boundary around objects. Each object is in one division. Home cannot be deleted.", "url": "https://help.genesys.cloud/articles/divisions-overview/", "source": "Divisions overview"},
        {"term": "All division", "def": "The org-wide grant. Use it on purpose.", "url": "https://help.genesys.cloud/articles/divisions-overview/", "source": "Divisions overview"},
        {"term": "Queue", "def": "The waiting line. Unique name, one division, up to 5000 members.", "url": "https://help.genesys.cloud/articles/create-queues/", "source": "Create queues"},
        {"term": "ACD skill", "def": "A label on an agent used by evaluation and bullseye. Not the same object as the queue.", "url": "https://help.genesys.cloud/articles/acd-evaluation-routing-methods/", "source": "Evaluation methods"},
        {"term": "Utilization", "def": "How many interactions of each media an agent may hold. Defaults include one voice and one callback.", "url": "https://help.genesys.cloud/articles/utilization/", "source": "Agent utilization"},
        {"term": "After call work", "def": "Time after an interaction for notes and wrap-up. Modes include optional, mandatory discretionary, and time-boxed.", "url": "https://help.genesys.cloud/articles/create-queues/", "source": "Create queues"},
        {"term": "ININ-WRAP-UP-TIMEOUT", "def": "The system wrap-up code when ACW ends before an agent picks a code.", "url": "https://help.genesys.cloud/articles/create-queues/", "source": "Create queues"},
        {"term": "Conversation score", "def": "Arrival time minus priority times 60000 ms. Higher priority waits less.", "url": "https://help.genesys.cloud/articles/create-queues/", "source": "Create queues"},
        {"term": "Priority score", "def": "Rank by priority, then by time in queue. Cross-queue, these queues take precedence.", "url": "https://help.genesys.cloud/articles/create-queues/", "source": "Create queues"},
        {"term": "Bullseye routing", "def": "Up to five rings. Delay from 2 seconds to 72 hours. Remove up to 50 skills as rings expand.", "url": "https://help.genesys.cloud/articles/bullseye-routing-overview/", "source": "Bullseye routing"},
        {"term": "Preferred agent routing", "def": "Try preferred agents first, even without the skill, if they are queue members and On Queue.", "url": "https://help.genesys.cloud/articles/preferred-agent-routing-behavior/", "source": "Preferred agent routing"},
        {"term": "Predictive routing", "def": "A KPI model with a timeout back to standard routing, and a 30-day quiet period that disables it.", "url": "https://help.genesys.cloud/articles/advanced-routing-overview/", "source": "Advanced routing"},
        {"term": "Architect", "def": "The flow designer. Runtime uses the published version, not the draft.", "url": "https://help.genesys.cloud/articles/about-architect/", "source": "About Architect"},
        {"term": "In-queue flow", "def": "The hold experience. The default call flow exists and does nothing until you publish it.", "url": "https://help.genesys.cloud/articles/queue-call-flows/", "source": "In-queue flows"},
        {"term": "Common module", "def": "A reusable Architect flow so you do not copy the same task into every inbound flow.", "url": "https://help.genesys.cloud/articles/create-a-flow/", "source": "Create a flow"},
        {"term": "Secure call flow", "def": "Collects sensitive digits away from the recording. Not a place to copy digits into participant data.", "url": "https://help.genesys.cloud/articles/create-a-flow/", "source": "Create a flow"},
        {"term": "BYOC Cloud", "def": "Your carrier, Genesys media, no customer Edge on the media path.", "url": "https://help.genesys.cloud/articles/about-byoc-cloud/", "source": "About BYOC Cloud"},
        {"term": "BYOC Premises", "def": "A customer Edge terminates local phones and trunks.", "url": "https://help.genesys.cloud/articles/edge-groups-overview/", "source": "Edge groups"},
        {"term": "Dynamic Cloud Voice", "def": "The current platform for new BYOC Cloud trunks.", "url": "https://help.genesys.cloud/articles/dynamic-cloud-voice-platform-overview/", "source": "Dynamic Cloud Voice"},
        {"term": "Edge group", "def": "Edges that share phones and trunks for a site. Local site routing prefers them.", "url": "https://help.genesys.cloud/articles/edge-groups-overview/", "source": "Edge groups"},
        {"term": "Number plan", "def": "Classifies a dial string. Up to 200 per site. Emergency is one of the defaults.", "url": "https://help.genesys.cloud/articles/number-plan-information/", "source": "Number plans"},
        {"term": "E.164", "def": "The international number form several plan types normalize toward.", "url": "https://help.genesys.cloud/articles/number-plan-information/", "source": "Number plans"},
        {"term": "WEM", "def": "Workforce engagement management: recording, quality, performance, analytics, and workforce management.", "url": "https://help.genesys.cloud/articles/about-workforce-engagement-management-wem/", "source": "About WEM"},
        {"term": "Service goal template", "def": "The planning target for workforce management, including service level as a percent in a number of seconds.", "url": "https://help.genesys.cloud/articles/about-workforce-engagement-management-wem/", "source": "About WEM"},
        {"term": "Quality management", "def": "Forms, policies, calibration, coaching, and disputes.", "url": "https://help.genesys.cloud/50540/", "source": "About quality management"},
        {"term": "Speech and text analytics", "def": "Transcription and analysis of voice and digital interactions, including topics and sentiment.", "url": "https://help.genesys.cloud/articles/speech-and-text-analytics-overview/", "source": "STA overview"},
        {"term": "Agent Copilot", "def": "Agent-facing assistance: knowledge, transcripts, scripts, next best action, and notes. A CX 4 addition on the overview.", "url": "https://help.genesys.cloud/articles/agent-copilot-overview/", "source": "Agent Copilot"},
        {"term": "Dialog Engine Bot Flow", "def": "An Architect bot type the inbound flow calls with Call Bot Flow.", "url": "https://help.genesys.cloud/articles/about-genesys-dialog-engine-bot-flows/", "source": "Dialog Engine bots"},
        {"term": "Digital Bot Flow", "def": "An Architect bot type for messages, called with Call Digital Bot Flow.", "url": "https://help.genesys.cloud/articles/about-genesys-digital-bot-flows/", "source": "Digital bot flows"},
        {"term": "Client credentials", "def": "An OAuth grant for a service. The token cannot call /api/v2/users/me.", "url": "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials", "source": "Client credentials"},
        {"term": "Authorization code", "def": "The grant for an app that acts as a user. Use PKCE when the article requires it.", "url": "https://help.genesys.cloud/articles/create-an-oauth-client/", "source": "OAuth client"},
        {"term": "Implicit grant", "def": "Token Implicit Grant, documented as deprecated after 25 May 2026.", "url": "https://help.genesys.cloud/articles/create-an-oauth-client/", "source": "OAuth client"},
        {"term": "AppFoundry", "def": "The marketplace. A listing does nothing until it is installed.", "url": "https://appfoundry.genesys.com/", "source": "AppFoundry"},
        {"term": "Fair use", "def": "Monthly pooled allowances with no rollover. This lab does not copy dollar rates.", "url": "https://help.genesys.cloud/articles/genesys-cloud-fair-use-policy/", "source": "Fair use policy"},
        {"term": "Named user", "def": "A license assigned to a person. The CX 4 overview lists 30 AI tokens for a named user.", "url": "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/", "source": "Overview"},
        {"term": "Concurrent user", "def": "A license based on peak usage. The overview lists 39 AI tokens. Billing discards peaks under 30 minutes.", "url": "https://help.genesys.cloud/articles/concurrent-licensing-model-billing-overview/", "source": "Concurrent billing"},
        {"term": "GC-GCP", "def": "Genesys Cloud Professional Certification, one exam, on the current catalog.", "url": CATALOG, "source": "Genesys Cloud exams"},
        {"term": "GC-GCD", "def": "Genesys Cloud Developer Certification, one exam, on the current catalog.", "url": CATALOG, "source": "Genesys Cloud exams"},
        {"term": "RFC 5737", "def": "Documentation IPv4 ranges. Synthetic logs in this lab use them and must not be pasted into a trunk ACL.", "url": "https://www.rfc-editor.org/rfc/rfc5737", "source": "RFC 5737"},
    ],
    "bosses": [],
    "interviews": [],
}


def _boss(bid, title, severity, brief, steps, fix, url, source):
    REFERENCE["bosses"].append({
        "id": bid,
        "title": title,
        "severity": severity,
        "brief": brief,
        "steps": steps,
        "fix": fix,
        "url": url,
        "source": source,
    })


def _step(log, ask, choices, answer, why):
    return {"log": log, "ask": ask, "choices": choices, "answer": answer, "why": why}


_boss(
    "b-login",
    "Agents are in the wrong region",
    "Sev-2",
    "A new class signs into US East. The organization was created in US West. Synthetic log, not a customer capture.",
    [
        _step(
            "09:14Z auth failed user.a@example.invalid host=login.mypurecloud.com orgRegion=us-west-2 expectedLogin=login.usw2.pure.cloud src=203.0.113.10",
            "Which host matches the organization?",
            ["login.mypurecloud.com, because it is the oldest name", "login.usw2.pure.cloud", "login.use2.us-gov-pure.cloud", "api.mypurecloud.com as a login page"],
            1,
            "US West’s documented login host is login.usw2.pure.cloud. US East is login.mypurecloud.com.",
        ),
        _step(
            "09:16Z token aud=us-east-1 used against org us-west-2 result=unauthorized",
            "What is wrong with the token?",
            ["It was minted for a different core region than the org", "Satellite media rejected it", "The queue has 5001 members", "Bullseye ring 6 is required"],
            0,
            "Login host and API host are a pair for the org’s core region.",
        ),
        _step(
            "09:20Z bookmark still says login.mypurecloud.com. No satellite region involved.",
            "What do you change first?",
            ["Move the org to us-east-1 overnight", "Replace the bookmark with the US West login host", "Delete the Home division", "Turn on implicit grant"],
            1,
            "Send users to the login host on the regions article for that org. Do not invent an API hostname.",
        ),
    ],
    "Point the class at login.usw2.pure.cloud and confirm the API host on the regions article before any client is configured. Do not guess an API hostname.",
    "https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/",
    "AWS regions",
)

_boss(
    "b-prefer",
    "The preferred agent never rings",
    "Sev-3",
    "Amina is preferred and idle. Leo, who has been idle longer, keeps taking the calls. Synthetic agent names.",
    [
        _step(
            "queue=Billing method=Preferred evaluation=All skills agent=Amina onQueue=false preferred=true skills=Billing",
            "Why is Amina skipped?",
            ["Preferred agents are never selected", "Amina is not On Queue", "Conversation score forbids preferred agents", "The name is longer than 200 characters"],
            1,
            "Preferred routing still requires a queue member who is On Queue.",
        ),
        _step(
            "agent=Leo onQueue=true preferred=false idleMs=120000 skills=Billing,Spanish agent=Amina idleMs=40000",
            "Once Amina is On Queue, who should be offered first?",
            ["Leo, because idle time is higher", "Amina, the preferred agent, even if a skill is missing", "Nobody, until bullseye ring 6", "The most recently hired agent"],
            1,
            "Preferred agents are considered first, including when they lack a required skill.",
        ),
        _step(
            "Amina utilization voice=1/1. Interaction is a second voice call.",
            "She is On Queue and preferred, and still skipped. Why?",
            ["Full utilization excludes her", "Preferred routing ignores utilization", "The Edge is required for preferred", "ACW codes block preferred agents"],
            0,
            "An agent at voice capacity is not offered another voice interaction.",
        ),
    ],
    "Set Amina On Queue, keep her under the voice utilization limit, and confirm she is a member of the queue. Preferred routing does not bypass those gates.",
    "https://help.genesys.cloud/articles/preferred-agent-routing-behavior/",
    "Preferred agent routing",
)

_boss(
    "b-rings",
    "Bullseye never leaves the inner ring",
    "Sev-2",
    "Spanish-speaking callers wait behind an English-only inner ring until they abandon. The delay was copied from a different unit.",
    [
        _step(
            "method=Bullseye rings=2 ring1.delaySec=259200 ring2.remove=Spanish elapsedSec=900 matchingAgents=0",
            "Why is ring 2 still closed after 15 minutes?",
            ["The delay is 72 hours, the top of the documented range, so 15 minutes is still ring 1", "Rings cannot remove skills", "Five is the minimum ring count", "Priority score disables bullseye"],
            0,
            "Bullseye delays run from 2 seconds to 259200 seconds. A 72 hour delay will not expand during a normal wait.",
        ),
        _step(
            "Corrected ring1.delayMs=20000. ring2.remove=Spanish. elapsedMs=21000. Agents with Billing only: 4.",
            "After the delay, which skill is still required?",
            ["Spanish", "Billing", "Both", "Neither"],
            1,
            "The outer ring removes Spanish. Billing stays because it was not removed.",
        ),
        _step(
            "Design proposes 9 rings to mirror a UCCE precision queue.",
            "What is the Genesys cap?",
            ["50 rings", "5 rings", "1 ring", "200 rings"],
            1,
            "Bullseye allows up to five rings. Fifty is the cap on skills removed, not on rings.",
        ),
    ],
    "Set the inner-ring delay in seconds inside the documented range, remove only the skill you mean to relax, and keep the design at five rings or fewer.",
    "https://help.genesys.cloud/articles/bullseye-routing-overview/",
    "Bullseye routing",
)

_boss(
    "b-acl",
    "The carrier lost the new media addresses",
    "Sev-1",
    "After a Dynamic Cloud Voice change, inbound calls never reach Architect. The lab log uses a documentation address, not a real ingress prefix.",
    [
        _step(
            "trunk=byoc-cloud signaling=timeout remote=198.51.100.20 note=synthetic-doc-address acl=stale-list platform=DCVP",
            "Which platform article do you open before touching the ACL?",
            ["The implicit-grant deprecation", "Dynamic Cloud Voice platform overview", "The STA dialect table", "GC-GCP course 135"],
            1,
            "New BYOC Cloud trunks and this class of move belong to Dynamic Cloud Voice. Copy the current allowlist from that guidance, not from a ticket.",
        ),
        _step(
            "Architect inbound flow=published. Queue=staffed. Edge=none. Carrier SBC shows SYN to the old destination only.",
            "Where is the break?",
            ["The in-queue flow", "Between the carrier and the new cloud ingress", "Agent utilization", "A missing topic"],
            1,
            "Published flows never see a call the carrier is still sending to the old address.",
        ),
        _step(
            "Someone pastes 203.0.113.50 into the carrier ACL from this lab’s sample.",
            "Why is that harmful?",
            ["RFC 5737 addresses are documentation ranges, not Genesys ingress", "It is the required anycast address", "It fixes SRTP", "It publishes the flow"],
            0,
            "Synthetic logs are not an allowlist. Use the current article.",
        ),
    ],
    "Update the carrier allowlist and remote targets from the current Dynamic Cloud Voice guidance, place a test call, and only then move production numbers.",
    "https://help.genesys.cloud/articles/dynamic-cloud-voice-platform-overview/",
    "Dynamic Cloud Voice",
)

_boss(
    "b-hold",
    "Answered calls, then silence on hold",
    "Sev-2",
    "The inbound menu works. Callers who wait hear nothing and hang up.",
    [
        _step(
            "inbound=Billing published=true inQueue=Default Call Flow published=false queue.media=call",
            "What is the hold path doing?",
            ["It is live because a default exists", "It is not published, so it does not run", "It is a bot flow", "It is an Edge group"],
            1,
            "The default in-queue call flow is not auto-published.",
        ),
        _step(
            "Published a draft that contains a menu and a reusable task inside the in-queue call flow. Validation errors.",
            "What does the in-queue call article allow as the treatment?",
            ["Menus and reusable tasks", "A music action, without those extras", "A secure payment form", "A precision queue"],
            1,
            "In-queue call flows are the hold experience, not a second IVR.",
        ),
        _step(
            "Music plays. Agents are Off Queue. Alerting does not start.",
            "Why is there still no agent?",
            ["The flow replaced ACD", "Nobody is On Queue", "Conversation score is negative", "The login host is wrong"],
            1,
            "The hold flow can be perfect while the queue has no eligible agent.",
        ),
    ],
    "Publish an in-queue call flow that plays music, put agents On Queue, and test both the menu and the wait before you move a production number.",
    "https://help.genesys.cloud/articles/queue-call-flows/",
    "In-queue flows",
)

_boss(
    "b-me",
    "The health check calls users/me",
    "Sev-3",
    "A service page fires every minute. The token is client credentials. The check expects a user.",
    [
        _step(
            "POST /oauth/token grant_type=client_credentials host=login.mypurecloud.com result=200",
            "Did login succeed?",
            ["No, client credentials are invalid", "Yes. The failure is the next call.", "Only if PKCE was used", "Only for implicit grant"],
            1,
            "The token was issued. The grant is the problem for the following path.",
        ),
        _step(
            "GET /api/v2/users/me host=api.mypurecloud.com status=403 body.labIllustration=true",
            "Why does that path fail?",
            ["The API host for US East is wrong", "A client-credentials token has no user", "Queues cannot be named Billing", "The Edge is offline"],
            1,
            "The client-credentials guide documents this limit.",
        ),
        _step(
            "The same client can GET /api/v2/users when the role allows it.",
            "What should the health check call instead?",
            ["A resource the service role can read, or switch to authorization code if it must be a user", "/oauth/token with a password in the query", "The implicit grant hash", "A SIP OPTIONS to the PSAP"],
            0,
            "Do not keep calling users/me with a service token.",
        ),
    ],
    "Change the probe to an API the role allows, or replace the grant with authorization code if the call must run as a person. Rotate the secret if it was pasted into a ticket.",
    "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials",
    "Client credentials",
)

_boss(
    "b-qm",
    "Quality has a form and no audio",
    "Sev-3",
    "Evaluators open a form and find silence. AI scoring is also empty.",
    [
        _step(
            "recordingPolicy=none queue=Billing transcription=on tokens=present form=Customer care",
            "What is missing for a human evaluation?",
            ["A recording policy that actually records", "A fifth bullseye ring", "An implicit grant", "A satellite region"],
            0,
            "Quality management evaluates recordings. No policy means no audio.",
        ),
        _step(
            "AI scoring status=skipped reason=no transcript segment. transcription was enabled only on a different queue.",
            "Which FAQ gates are still unsatisfied?",
            ["None. Tokens are enough.", "Speech and text analytics on this interaction, plus QM and tokens", "Only GC-GCP", "Only the Edge"],
            1,
            "The STA FAQ requires the transcript, quality management, and AI Experience Tokens.",
        ),
        _step(
            "Secure flow collected a card number into participant data so the form could score it.",
            "What rule was broken?",
            ["Secure flows exist so digits stay out of recordings and participant data", "Participant data is the recommended PCI store", "Scores require the PAN", "Copilot must see the PAN"],
            0,
            "Do not copy payment digits into participant data.",
        ),
    ],
    "Attach a recording policy to the queue, confirm transcription on that same queue, and keep payment digits inside the secure flow.",
    "https://help.genesys.cloud/articles/about-recording/",
    "About recording",
)

_boss(
    "b-implicit",
    "A widget still uses the implicit grant",
    "Sev-2",
    "The OAuth article’s deprecation date has a client on the wrong side of it. Synthetic client name.",
    [
        _step(
            "oauthClient=desktop-widget grant=token-implicit installed=2024-11-01 articleDeprecation=2026-05-25",
            "What does the article say about this grant?",
            ["It is the recommended grant for new SPAs", "It is deprecated after 25 May 2026", "It can call users/me without a user", "It replaces client credentials for SCIM"],
            1,
            "Do not start new work on Token Implicit Grant, and plan the move.",
        ),
        _step(
            "The widget acts as the signed-in agent. A teammate suggests pasting a long-lived token into a data action.",
            "What is the replacement grant?",
            ["Authorization code with PKCE", "A password stored in the flow", "No OAuth", "SAML inside RTP"],
            0,
            "A user-facing app moves to authorization code. A service moves to client credentials.",
        ),
        _step(
            "Salesforce data action still uses a username and password. The embed itself is fine.",
            "Which guide applies to the action?",
            ["The Zendesk about page", "The Salesforce OAuth client-credentials migration guide", "The bullseye overview", "The number-plan page"],
            1,
            "The embed and the data action are different credentials. The migration guide keeps the action body and changes the auth.",
        ),
    ],
    "Move the widget to authorization code with PKCE, and move the Salesforce data action to the OAuth client-credentials flow with the consumer key, secret, and My Domain URL.",
    "https://help.genesys.cloud/articles/create-an-oauth-client/",
    "Create an OAuth client",
)


INTERVIEW = [
    ("Where does a Genesys Cloud organization live?", "In one core AWS region, with that region’s login host. Satellite regions carry media and cannot host the org. US East uses login.mypurecloud.com. US West uses login.usw2.pure.cloud. FedRAMP uses login.use2.us-gov-pure.cloud. Confirm every other host on the regions article.", "https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/", "AWS regions"),
    ("What do the four CX packages add, in order?", "CX 1 is voice, including secure IVR, callbacks, and campaigns. CX 2 adds digital channels and quality. CX 3 adds WEM and transcription minutes. CX 4 adds Agent Copilot, Journey Management, and the published token allotment of 30 named and 39 concurrent.", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/", "Overview"),
    ("What is a division?", "The boundary around configuration objects. An object is in one division. Home cannot be deleted. All is the org-wide grant. Roles are granted as role and division pairs.", "https://help.genesys.cloud/articles/divisions-overview/", "Divisions overview"),
    ("What limits apply when you create a queue?", "A unique name without special characters, a single division, and up to 5000 members. Voice alerting is 7 to 59 seconds. Copy settings if you need a twin, and check what the copy actually brought.", "https://help.genesys.cloud/articles/create-queues/", "Create queues"),
    ("Name the routing methods.", "Standard, predictive, bullseye, preferred agent, and conditional group routing. Standard is the default. Predictive timing out falls back to standard.", "https://help.genesys.cloud/articles/advanced-routing-overview/", "Advanced routing"),
    ("How does all-skills matching pick an agent?", "Among agents who have every required skill, are On Queue, and are under utilization, it picks the longest idle.", "https://help.genesys.cloud/articles/acd-evaluation-routing-methods/", "Evaluation methods"),
    ("How does best available skills differ?", "It takes up to the 100 longest-idle agents who match, then ranks them by average proficiency, with idle time as the tie-break.", "https://help.genesys.cloud/articles/acd-evaluation-routing-methods/", "Evaluation methods"),
    ("What is a conversation score?", "arrived time minus priority times 60000 milliseconds, so one priority point is one minute. Priority-score queues outrank conversation-score queues when both are in play.", "https://help.genesys.cloud/articles/create-queues/", "Create queues"),
    ("What are bullseye’s caps?", "Up to five rings, a delay from 2 seconds to 259200 seconds, and up to 50 skills removed on expansion. The inner ring keeps its priority.", "https://help.genesys.cloud/articles/bullseye-routing-overview/", "Bullseye routing"),
    ("When is a preferred agent skipped?", "When they are not a member, not On Queue, or at utilization. Transfers do not use preferred routing. A non-member does not sit through the preferred timeouts.", "https://help.genesys.cloud/articles/preferred-agent-routing-behavior/", "Preferred agent routing"),
    ("What has to be true before an Architect flow answers?", "It is published. A saved draft does not run. The default in-queue call flow exists and still needs a publish. Message and email flows need an error-event queue.", "https://help.genesys.cloud/articles/create-a-flow/", "Create a flow"),
    ("How do you call a bot and still survive a miss?", "Call Bot Flow for a Dialog Engine bot, or Call Digital Bot Flow for a digital bot. Bind no-match, timeout, and error to a queue. Confirm external connectors in Architect rather than from memory.", "https://help.genesys.cloud/articles/use-architect-to-create-a-bot-for-an-inbound-flow/", "Inbound bot"),
    ("What is BYOC Cloud?", "Your carrier’s SIP, Genesys cloud media, and no customer Edge on that path. New trunks use Dynamic Cloud Voice. Allowlist the current egress ranges rather than a copied list.", "https://help.genesys.cloud/articles/about-byoc-cloud/", "About BYOC Cloud"),
    ("When does another site’s Edge take a call?", "Local site routing stays on the local Edge group until those Edges are offline, at capacity, or missing the resource.", "https://help.genesys.cloud/articles/edge-groups-overview/", "Edge groups"),
    ("Who provides emergency calling on BYOC?", "Not Genesys. You classify the dial string, build the emergency route, and test it. Do not invent a backup PSAP number.", "https://help.genesys.cloud/articles/set-up-emergency-services-with-byoc/", "BYOC emergency"),
    ("What does a recording policy decide?", "Which ACD calls are recorded and how long they are kept. A secure flow can suppress a payment segment. It does not replace the policy.", "https://help.genesys.cloud/articles/about-recording/", "About recording"),
    ("What does AI scoring require?", "Speech and text analytics, quality management, and AI Experience Tokens. The FAQ’s token ratio should be re-read before you budget. A Copilot summary reused by Virtual Supervisor is not billed twice.", "https://help.genesys.cloud/faqs/category/speech-and-text-analytics/", "STA FAQ"),
    ("What does Agent Copilot show the agent?", "Knowledge articles, transcripts, custom scripts, next best action, and notes such as reason, resolution, and a possible wrap-up. The overview says the benefit can survive a blind transfer. It is not a secure payment flow.", "https://help.genesys.cloud/articles/agent-copilot-overview/", "Agent Copilot"),
    ("Which OAuth grant does a service use?", "Client credentials. Send the id and secret as HTTP Basic to the login host. The token cannot call /api/v2/users/me. Role and division pairs are a subset of the creator’s rights.", "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials", "Client credentials"),
    ("What happened to the implicit grant?", "The OAuth client article documents Token Implicit Grant as deprecated after 25 May 2026. User-facing apps move to authorization code with PKCE.", "https://help.genesys.cloud/articles/create-an-oauth-client/", "OAuth client"),
    ("How do you migrate a Salesforce data action off a password?", "Follow the Salesforce OAuth client-credentials migration guide: consumer key, secret, and My Domain URL. The action’s request body can stay. Re-test. The CX Cloud OAuth settings article is a different page.", "https://help.genesys.cloud/articles/salesforce-oauth-client-credentials-flow-migration-guide/", "Salesforce OAuth migration"),
    ("How do Engage and PureConnect move to Genesys Cloud?", "Rebuild Architect flows and queues. This lab has not found a one-click import. Confirm lifecycle dates on a Genesys notice, not on a community post.", "https://help.genesys.cloud/articles/about-architect/", "About Architect"),
    ("How do you explain a UCCE skill group to a Genesys design?", "As queue membership plus skills, not as one object. A precision queue is only an analogy for bullseye, and the ring caps stay on the Genesys article.", "https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html", "Cisco UCCE"),
    ("Which exam codes will you say out loud?", "GC-GCP for the professional exam and GC-GCD for the developer exam, because the catalog names them. Specialist and AI exams are named from the catalog without a GCX- prefix. Re-read the announcement before you book.", "https://education.genesys.com/certification/cloud", "Genesys Cloud exams"),
]

for question, answer, url, source in INTERVIEW:
    REFERENCE["interviews"].append({"q": question, "a": answer, "url": url, "source": source})
