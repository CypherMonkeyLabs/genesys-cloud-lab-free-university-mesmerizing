from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "emergency",
    "title": "Numbers and emergency calling",
    "kicker": "Safety",
    "accent": 1,
    "summary": "E.164, emergency classifications, BYOC warnings, and Genesys Cloud Voice coverage.",
    "lessons": [],
}
def add(item):
    TRACK["lessons"].append(item)

add(lesson(
    "n-owner", "Name the emergency owner before the DID", "Core", 12,
    "Genesys is not responsible for emergency calls that ride a BYOC trunk. That sentence belongs in the design, not in the postmortem.",
    [
        "The BYOC emergency article covers BYOC Cloud and BYOC Premises. You can dial the local emergency number, such as 911 in the United States, only after the carrier and the Genesys number plan and outbound route are both configured. If you also have Genesys Cloud Voice, its emergency information is not sent to the BYOC carrier. You tell the carrier the physical location yourself.",
        "Under BYOC Cloud and some premises configurations the emergency path is on the internet. A power cut or a broadband cut can take it away. The article says that plainly. A design that assumes the Edge or the laptop will always reach a PSAP is not the article.",
    ],
    cites("emergency", "gcv-regions"),
    fig("Two products, two emergency owners.", [
        ("g", "GCV", "region", 22, 40),
        ("b", "BYOC", "trunk", 55, 40),
        ("p", "PSAP", "carrier", 84, 40),
    ], [("g", "p"), ("b", "p")]),
    "Write the owner on the number",
    [
        ("Number", "Model", "GCV or BYOC", "The owner follows the model.", "Do not guess"),
        ("BYOC", "Carrier", "Send the address", "Genesys will not forward the GCV record.", "Physical location"),
        ("Site", "Plan", "Emergency class", "911, 933, or the local number.", "Plus an emergency route"),
        ("Risk", "Internet", "Document the outage case", "Broadband down means this path may be down.", "Say so in the runbook"),
    ],
    [
        q("Genesys’ warning on BYOC emergency calls is:", "Genesys is not responsible when emergency calls use BYOC trunks", ["Genesys is the PSAP", "Emergency is unsupported on GCV", "911 is a wrap-up code"], "The article states the warning."),
        q("GCV emergency data follows a BYOC number automatically?", "No", ["Yes", "Only for 933", "Only in satellite regions"], "You inform the BYOC carrier yourself."),
        q("BYOC Cloud emergency service can fail when:", "Power or broadband is down, because the path is on the internet", ["The queue name has a space", "Bullseye has two rings", "A bot is published"], "The article names those outages."),
        q("The Genesys-side configuration lives in:", "The site number plan and the emergency outbound route", ["The OAuth client", "The evaluation form", "The fair use table"], "The article points at those sections."),
        q("911 in the United States is used in the article as:", "An example of a regular emergency dialing number", ["A queue", "A skill", "A region"], "Other countries use their own numbers. 142 is the Swiss example on the number-plan page."),
        q("A runbook that omits the carrier address for a BYOC number is:", "Incomplete", ["Fine if the flow is published", "Required by RFC 3550", "A CX 1 feature"], "The carrier needs the physical location."),
    ],
    [("Warning", "BYOC emergency is not Genesys’ service."), ("No copy", "GCV records do not move to the BYOC carrier."), ("Internet", "Power and broadband can remove the path."), ("Configure", "Number plan and emergency route.")],
    "Label one DID",
    ["Model.", "Emergency owner.", "Location you will send the carrier, if BYOC.", "The outage case you will write down."],
    "The label has an owner and an outage case.",
    ("Assumed PSAP", "A BYOC pilot dials 911 and the carrier has no location.", "Number plan: 911 present. Carrier paperwork: empty.", "The plan without the carrier record is half the article.", "Stop the pilot until the carrier confirms the address and a test process the carrier accepts."),
))

add(lesson(
    "n-plan", "Emergency is a classification and a route", "Core", 12,
    "The default Emergency plan matches 911 and 933 in the US and Canada, and 142 in Switzerland. It still needs a route.",
    [
        "The number-plan article lists those defaults and the Suicide Prevention classification for 988 to +18002738255. Matching is not routing. The outbound route for the Emergency classification has to point at a trunk that can actually complete the call. An empty route is a matched number that goes nowhere.",
        "933 is included alongside 911 in that default. Treat 933 as part of the documented US and Canada emergency classification, and re-read the page before you tell a tester which number to dial. Custom plans can shadow these defaults if you put a broader regex in front of them.",
    ],
    cites("numbers", "emergency"),
    fig("Match, then route. A match alone does not leave the building.", [
        ("d", "911", "phone", 16, 40),
        ("c", "Emergency class", "architect", 48, 40),
        ("r", "Route", "trunk", 80, 40),
    ], [("d", "c"), ("c", "r")]),
    "Prove the route, not only the match",
    [
        ("Admin", "Plan", "See Emergency", "911 and 933 for US and Canada.", "142 for Switzerland"),
        ("Admin", "Route", "Assign a trunk", "The classification needs an outbound route.", "Empty is a dead end"),
        ("Admin", "988", "Leave the default", "Unless you have a reviewed reason.", "Custom regex can shadow it"),
        ("Test", "Simulator", "Then a controlled test", "The product has a call simulator.", "Live tests follow the carrier’s rules"),
    ],
    [
        q("US and Canada emergency defaults named on the number-plan page include:", "911 and 933", ["Only 112", "Only 000", "Only extension 4"], "933 is in that default."),
        q("142 is documented as:", "The Swiss emergency example", ["A US state code", "A bullseye ring", "A token"], "The number-plan article says so."),
        q("A matched emergency number with no route:", "Does not complete", ["Completes on any trunk", "Becomes a callback", "Publishes a flow"], "Classification and route are both required."),
        q("988’s documented default destination is:", "+18002738255", ["The first queue", "911", "The Edge"], "Confirm on the page before you depend on it."),
        q("A custom regex ahead of the emergency plan can:", "Shadow the default", ["Increase the member cap", "Change the AWS region", "Disable ACW"], "Order matters."),
        q("The in-product tool the number-plan article mentions for testing destinations is:", "The call simulator", ["Flow Insights", "The concurrent bill", "The quiz"], "Use it."),
    ],
    [("911 and 933", "US and Canada defaults."), ("142", "Swiss example."), ("Route", "Still required."), ("988", "Default destination is documented. Re-read it.")],
    "Check the emergency route",
    ["Name the classification.", "Name the trunk on the route.", "Say what a shadowing regex would do.", "Say which test tool you would use first."],
    "Match and route are both filled in.",
    ("Shadowed 911", "A lab regex ^9 sends 911 to a test queue.", "Custom plan ordered before Emergency.", "The default never sees the digits.", "Delete the lab plan and retest 911 in the call simulator."),
))

add(lesson(
    "n-location", "The location is a physical place", "Core", 11,
    "The quick start adds a location because services, including emergency, need a real site.",
    [
        "A location is not a division and not a site’s nickname. The BYOC quick start says you specify a physical location for the site, and the emergency article says the carrier needs the exact place the numbers are used. A downtown billing address for a warehouse an hour away is the kind of mistake that sends responders to the wrong door.",
        "Global Media Fabric and the site’s Edges should agree with that same geography. A location in one city and a media path pinned across an ocean is a latency choice you should make on purpose, not by default.",
    ],
    cites("byoc-quick", "emergency", "regions"),
    fig("The address responders would use is the location you send.", [
        ("loc", "Location", "phone", 22, 40),
        ("site", "Site", "edge", 52, 40),
        ("car", "Carrier", "carrier", 82, 40),
    ], [("loc", "site"), ("site", "car")]),
    "Send the address you mean",
    [
        ("Admin", "Location", "Street address", "The quick start’s step.", "Not a PO box story"),
        ("Admin", "Site", "Attach it", "The site points at the location.", "Edges live with the site"),
        ("Carrier", "Record", "Same address", "BYOC does not inherit GCV.", "You send it"),
        ("Review", "Walk", "Could a responder find the door", "If not, the record is wrong.", "Fix it before go-live"),
    ],
    [
        q("The location in the quick start is:", "A physical place for the site", ["The AWS region name", "The queue division", "The OAuth redirect"], "It enables services and supports emergency."),
        q("A billing PO box as the emergency location is:", "The wrong record if people are not there", ["Always correct", "Required", "A number plan"], "Responders need the place the numbers are used."),
        q("Who receives the BYOC location?", "Your carrier", ["Automatically every PSAP via GCV data", "The certification catalog", "AppFoundry"], "You inform the carrier."),
        q("Sites and locations are:", "Related telephony objects. A division is neither.", ["The same object", "Both OAuth grants", "Both skills"], "Do not collapse the vocabulary."),
        q("Media pinned far from the location is:", "A latency choice you should notice", ["Required", "Impossible", "A wrap-up code"], "The regions article discusses media placement for a reason."),
        q("The emergency article’s phrase “exact physical location” means:", "Where the numbers are actually used", ["The headquarters marketing address always", "The satellite region", "The agent’s home by default"], "Send the place people call from."),
    ],
    [("Physical", "Not a nickname."), ("Carrier", "You send it for BYOC."), ("Site", "Attaches the location."), ("Door test", "Could someone find it.")],
    "Write one location",
    ["Street and city.", "Which site.", "Which carrier record.", "The door test in one sentence."],
    "The address is a place a person can stand.",
    ("Headquarters for every branch", "Every branch DID has the HQ address.", "Carrier records: one address. Sites: twelve.", "Responders would go to the wrong building.", "Register each site’s own address with the carrier."),
))

add(lesson(
    "n-gcv-limits", "Voice coverage is a table, not a promise", "Advanced", 12,
    "Country rows decide DID, toll-free, domestic, and international. FedRAMP and the sovereign region add harder edges.",
    [
        "The restrictions article is a matrix of countries and call types, plus two special sections. FedRAMP can add US numbers and US domestic and international calling, and it cannot add other countries. The European Sovereign region’s sovereignty commitment does not cover voice that leaves the ESR boundary. Those calls use non-EU carriers and are outside the commitment.",
        "Planned regions on the Voice regions article, including notes about Mexico and Singapore in the table’s forward-looking rows, are not a contract. If the page says limited or coming, your design says limited or coming. The lab will not freeze that table.",
    ],
    cites("gcv-regions"),
    fig("Read the country row before you sell the number.", [
        ("row", "Country row", "region", 24, 40),
        ("did", "DID", "phone", 58, 22),
        ("intl", "International", "trunk", 58, 68),
    ], [("row", "did"), ("row", "intl")]),
    "Check a country before the order",
    [
        ("Seller", "Article", "Open the row", "DID, toll-free, domestic, international.", "Empty means no"),
        ("Seller", "FedRAMP", "US only", "Other countries are unavailable.", "Do not attach a foreign DID"),
        ("Seller", "ESR", "Boundary", "Outside means outside the commitment.", "Say that in the contract"),
        ("Seller", "Planned", "Not sold as live", "Reload the page.", "The lab does not copy the future"),
    ],
    [
        q("FedRAMP Genesys Cloud Voice for a non-US country is:", "Unavailable", ["The same as commercial Ireland", "Included in CX 1", "A number-plan default"], "The restrictions article says so."),
        q("An ESR call to a destination outside the boundary:", "Is not covered by the ESR sovereignty commitment", ["Is blocked by Architect", "Is free", "Uses only bullseye"], "The article describes non-EU handling."),
        q("The right artifact before ordering numbers is:", "The current country row", ["A 2023 PDF only", "A forum post", "The quiz score"], "Reload the restrictions page."),
        q("DID availability and international calling are:", "Separate columns", ["Always identical", "Both skills", "Both tokens"], "A country can differ by call type. Read the row."),
        q("A region marked coming or limited on the Voice page should be sold as:", "Coming or limited", ["Generally available worldwide", "A premises Edge", "A certification"], "Use the page’s words."),
        q("This lab does not paste the full country matrix because:", "The matrix changes and the page is the source", ["The matrix is secret", "There is no article", "RFCs forbid it"], "Link it."),
    ],
    [("Row", "DID, toll-free, domestic, international."), ("FedRAMP", "US voice services."), ("ESR", "Boundary is the commitment."), ("Coming", "Stay coming until the page changes.")],
    "Check two countries",
    ["Pick a country you know is in the table.", "Pick the FedRAMP constraint.", "Write the ESR boundary rule.", "Say you will reload the page before an order."],
    "The notes cite the article instead of a frozen matrix.",
    ("Foreign DID on FedRAMP", "An order for a non-US DID was submitted in the gov region.", "Restrictions: other countries unavailable.", "The row was not read.", "Cancel the order and use a region where that country is offered, if one exists on the current page."),
))

add(lesson(
    "n-e164", "Normalize toward E.164 on purpose", "Core", 11,
    "Intra-country and inter-country plans normalize. Digit-length extensions and E.164 lists do not.",
    [
        "The number-plan article is specific. Inter-country matches a country code and a length and normalizes to E.164. Intra-country uses the site’s country and does the same. Digit length for extensions does not normalize. An E.164 list entry must already contain the plus and is left alone. A number can pass through more than one plan and be normalized more than once.",
        "That is why a double-prefix bug shows up as +1+1555… in a trace. A later plan normalized something an earlier plan had already finished. The call simulator is how you see it before the carrier rejects it.",
    ],
    cites("numbers", "rfc5737"),
    fig("Some match types rewrite the number. Some must not.", [
        ("ext", "Extension", "phone", 18, 30),
        ("nat", "Intra-country", "architect", 50, 30),
        ("e", "E.164 list", "trunk", 82, 30),
    ], [("ext", "nat"), ("nat", "e")]),
    "Watch a number change",
    [
        ("User", "Dial", "10 digits", "Intra-country can add the country code.", "Plus and country code out"),
        ("User", "Dial", "4501", "Extension. No rewrite.", "4 to 6 digits"),
        ("Flow", "Transfer", "+15555550100", "Already E.164.", "A list match should not touch it"),
        ("Admin", "Simulator", "Look for a second plus", "Double normalization is a bug.", "Fix the plan order"),
    ],
    [
        q("Intra-country plans:", "Normalize to E.164 using the site country code", ["Never change the digits", "Only match 911", "Delete the trunk"], "The article describes that normalization."),
        q("A 5-digit extension:", "Matches digit length and is not normalized", ["Becomes E.164", "Becomes 988", "Becomes a queue"], "Digit length does not normalize."),
        q("An E.164 list entry must:", "Contain the plus, and it is not normalized", ["Be 4 digits", "Omit the plus", "Be a regex only"], "The article says so."),
        q("A number can be normalized:", "More than once if multiple plans touch it", ["Never", "Only by a bot", "Only in FedRAMP"], "The article allows multiple passes. That is how double prefixes happen."),
        q("555-0100 style numbers in this lab are:", "Fictional examples, not a customer", ["Your carrier’s test line", "The PSAP", "The API host"], "Do not dial them as a production test."),
        q("The tool that shows the rewrite before the carrier does is:", "The call simulator", ["Flow Insights", "The concurrent report", "The 3D map"], "Use the product tool."),
    ],
    [("Intra-country", "Adds the country code."), ("Extension", "No rewrite."), ("E.164 list", "Plus required, no rewrite."), ("Twice", "Possible, and often a bug.")],
    "Rewrite three strings by hand",
    ["A 10-digit national number.", "A 5-digit extension.", "A number that already has a plus.", "Say which one must not change."],
    "You can predict the simulator.",
    ("Double prefix", "The carrier rejects +1+15555550100.", "Two intra-country plans both normalize.", "The second pass treated the result as national again.", "Stop after the first successful E.164 normalization and retest in the simulator."),
))

add(lesson(
    "n-test", "Test emergency like a change, not like a demo", "Core", 12,
    "A live emergency test is a carrier and public-safety conversation. The call simulator is the part you can do alone.",
    [
        "Use the product call simulator for classification and normalization. Use a maintenance window and the carrier’s approved method before any live emergency test. The article’s warning about internet loss belongs in the test plan: if the broadband path is the only path, say what staff should do when it is down. That fallback is a life-safety procedure, and this lab will not invent a PSAP phone number for you.",
        "Record the model, the location, the route, and the result. An unlogged successful test is a rumor. An unlogged failed test is how the next site repeats it.",
    ],
    cites("numbers", "emergency"),
    fig("Simulator first. Live test only with the carrier’s method.", [
        ("sim", "Simulator", "architect", 22, 40),
        ("car", "Carrier method", "carrier", 55, 40),
        ("log", "Log", "wem", 84, 40),
    ], [("sim", "car"), ("car", "log")]),
    "Plan the test",
    [
        ("Admin", "Simulator", "911, 933, 988, extensions", "Classification only.", "No live PSAP yet"),
        ("Carrier", "Method", "Their process", "Do not freelance a live test.", "Location confirmed"),
        ("Ops", "Outage", "Write the broadband-down action", "The article says the path can vanish.", "Staff need a procedure"),
        ("Ops", "Log", "Model, route, result", "So the next site can read it.", "Rumor is not a result"),
    ],
    [
        q("The first test tool is:", "The call simulator", ["A live 911 call from a laptop", "A quiz", "A token"], "Classification can be proven without a PSAP."),
        q("A live emergency test should follow:", "The carrier’s approved method", ["A forum post", "An RFC example", "A bot intent"], "Do not improvise."),
        q("The internet-outage case must be:", "Written down, because the article says the path can be unavailable", ["Ignored", "Solved by publishing a flow", "Solved by bullseye"], "Staff need a procedure this lab does not invent for them."),
        q("An unlogged test is:", "Not a result the next site can trust", ["Better", "Required", "A certification"], "Write model, route, and result."),
        q("933 belongs in the simulator list for US and Canada because:", "It is part of the documented emergency classification", ["It is a queue", "It is a skill", "It is an extension"], "The number-plan page includes it."),
        q("This lab does not supply a backup PSAP number because:", "Inventing one would be dangerous and unsupported", ["PSAP numbers are skills", "911 is deprecated", "Edges block all emergency calls"], "Use local emergency services and the carrier’s process."),
    ],
    [("Simulator", "First."), ("Carrier", "Owns the live method."), ("Outage", "Write the broadband-down action."), ("Log", "Model, route, result.")],
    "Draft the test record",
    ["Simulator cases.", "Who approves a live test.", "The outage action’s owner.", "The four fields you will log."],
    "The record has a simulator section and a live section, and the live section has an approver.",
    ("Unapproved live test", "Someone dials 911 from the lab trunk to “see what happens.”", "No carrier window. No log.", "That is not the article’s process.", "Stop. Use the simulator. Schedule a carrier-approved test if one is required."),
))
