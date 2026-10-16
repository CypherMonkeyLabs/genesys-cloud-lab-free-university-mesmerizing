from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "forecast",
    "title": "Workforce and forecasting",
    "kicker": "Chapter",
    "accent": 2,
    "summary": "Forecast views, creation methods, the editor, and the short-term weeks that are allowed to build a schedule.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "n-place", "A forecast is a WFM plan for interactions, not a routing method", "Foundation", 12,
    "Workforce management is one WEM product. The forecast article names the metrics and the permissions.",
    [
        "The WEM article is the family: recording, quality, speech and text analytics, and workforce management. The forecast article is narrower. Forecasts help you plan how many interactions to expect. The metrics it names are pattern, volume as interactions offered, and average handle time made of average talk time, average hold time, and average after call work. That handle time is not the conversation-score priority on a queue.",
        "The forecast article lists these permissions: Workforce Management > Forecast – Add, Delete, Edit, and View; Analytics > conversationsAggregate – View; and Analytics > taskmanagementAggregate – View. The WFM track in this lab covers business units, schedules, adherence, and time off. This chapter stays on the forecast pages: views, creation methods, the editor, and what is allowed to generate a schedule.",
    ],
    cites("wem", "wfm-forecasts", "wfm-overview"),
    fig("WFM is inside WEM. The forecast feeds a schedule only from its short-term side.", [
        ("wem", "WEM", "wem", 16, 40),
        ("wfm", "WFM", "agent", 46, 40),
        ("f", "Forecast", "queue", 76, 40),
    ], [("wem", "wfm"), ("wfm", "f")]),
    "Separate the forecast from the route",
    [
        ("Family", "WEM", "Several products", "WFM is one of them.", "Quality is not a forecast"),
        ("Metric", "Volume", "Interactions offered", "AHT is talk, hold, and ACW.", "Not a bullseye ring"),
        ("Access", "Permissions", "Forecast and two analytics views", "Add, delete, edit, view.", "This lab does not grant them"),
        ("Next", "Chapter", "Views and methods", "The WFM track still has adherence.", "Read both"),
    ],
    [
        q("Volume on the forecast article means:", "Interactions offered", ["Agents On Queue", "Bullseye rings", "AI tokens"], "Average handle time is a different metric on the same page."),
        q("Average handle time there is composed of:", "Average talk, average hold, and average after call work", ["Only alert time", "Only adherence", "Priority times 60,000 ms"], "The article names those three averages."),
        q("The forecast permission family on that page is:", "Workforce Management > Forecast, plus two Analytics aggregate views", ["Routing > Queue only", "Quality > Evaluation Form only", "OAuth client credentials"], "The analytics views are conversationsAggregate and taskmanagementAggregate."),
        q("A forecast is not:", "The queue’s routing method", ["A WFM object", "A plan for later weeks", "Something the WEM family contains"], "Routing methods are on the queue. Forecasts are in workforce management."),
        q("This lab’s WFM track already covers:", "Business units, schedules, adherence, and time off", ["SIP TLS ciphers", "The implicit grant date", "Bullseye ring caps"], "This chapter does not replace that track."),
        q("WEM and WFM differ here because:", "WEM is the family and WFM is the product that holds forecasts", ["They are the same screen", "WFM is a trunk", "WEM is an RFC"], "The WEM article is the list. The forecast article is the plan."),
    ],
    [("Volume", "Interactions offered."), ("AHT", "Talk, hold, and after call work."), ("Permissions", "Forecast, plus two analytics views."), ("Not routing", "A forecast does not pick the agent.")],
    "Label three numbers",
    ["One volume.", "One handle time, with its three parts.", "One routing metric you will not store in the forecast.", "The permission you would need before you click Add."],
    "Handle time is not written down as a routing score.",
    ("Stolen metric", "A staffing sheet uses conversation-score priority as average handle time.", "The forecast page’s handle time is talk, hold, and after call work.", "The queue score was nearby.", "Replace the column with the three averages, or label it as a routing score and take it off the forecast."),
))

add(lesson(
    "n-views", "Short-term weeks can schedule. Long-term weeks cannot", "Foundation", 12,
    "Six weeks of intervals on one side. Up to two years of days and weeks on the other.",
    [
        "The forecast article describes two views. The short-term view is interval-level data, one week at a time, for up to six weeks depending on the forecast length, and it can generate schedules. The long-term view is day- and week-level data, up to one year at a time and up to two years total, for seasonality and trends. It cannot generate schedules. Schedules use only the short-term component, whose maximum is six weeks, so a longer horizon needs multiple forecasts.",
        "The forecasts list shows up to 26 weeks before and 26 weeks after the earlier of the current week or the last week that has a forecast. Search finds forecasts outside that window, including a start date up to 104 weeks in the future. You do not have to pick the exact start week. Available for Schedule is the checkbox that lets the forecast appear when you generate a schedule. The default time zone is the business unit’s, and an administrator can change the displayed zone.",
    ],
    cites("wfm-forecasts", "wfm-schedules", "forecast-editor"),
    fig("Only the short-term block is allowed to generate a schedule.", [
        ("s", "Short-term", "queue", 28, 28),
        ("l", "Long-term", "region", 28, 72),
        ("g", "Schedule", "agent", 78, 28),
    ], [("s", "g")]),
    "Point each view at a job",
    [
        ("Short", "Intervals", "Up to six weeks", "Can generate a schedule.", "One week on screen at a time"),
        ("Long", "Days and weeks", "Up to two years", "Seasonality.", "Cannot generate a schedule"),
        ("List", "Plus or minus 26 weeks", "Search goes further", "Up to 104 weeks ahead.", "Overlap is enough"),
        ("Flag", "Available for Schedule", "Off means hidden", "Generation will not offer it.", "Time zone defaults to the business unit"),
    ],
    [
        q("Which view can generate a schedule?", "The short-term view", ["The long-term view", "Both, at daily granularity", "Neither"], "The article says the long-term view cannot."),
        q("The short-term maximum used for scheduling is:", "Six weeks", ["Two years", "130 weeks", "26 weeks"], "Longer than six weeks needs multiple forecasts. 130 weeks is the create-page outer limit, not the scheduling slice."),
        q("The long-term view shows:", "Day and week data, up to one year at a time and two years total", ["15-minute intervals for two years", "A single interaction", "Bullseye rings"], "15, 30, and 60 minutes are the short-term editor granularities."),
        q("The on-screen list, before you search, spans:", "26 weeks back and 26 weeks forward from the earlier of now or the last forecast week", ["Only the current day", "104 weeks in both directions on the first paint", "Six rings"], "Search is what reaches 104 weeks into the future."),
        q("A forecast with Available for Schedule cleared:", "Does not appear as a choice when you generate a schedule", ["Becomes the long-term view", "Deletes the business unit", "Changes the routing method"], "The article says to enable the checkbox or it will not be offered."),
        q("The default time zone for the forecast view is:", "The business unit’s", ["UTC with no other choice", "The carrier’s", "The browser language"], "An administrator can pick another displayed zone. The business unit zone stays listed."),
    ],
    [("Short-term", "Up to six weeks, can schedule."), ("Long-term", "Seasonality, cannot schedule."), ("List", "26 weeks each way, then search."), ("Checkbox", "Available for Schedule.")],
    "Choose a view for three questions",
    ["How many intervals next Tuesday?", "Is December a high season?", "Can this forecast build next week’s shifts?", "Which control hides it from generation?"],
    "December is long-term, the shifts require the checkbox and the short-term weeks.",
    ("Year as a shift", "Someone generates a schedule from the long-term view because the season is obvious there.", "The article says that view cannot generate schedules.", "The six-week cap was ignored.", "Use a short-term forecast marked Available for Schedule, and add another forecast if the horizon is longer than six weeks."),
))

add(lesson(
    "n-methods", "Four creation methods, and a 130-week outer limit", "Core", 13,
    "Automatic best method, weighted history, imported source days, or a finished short-term file.",
    [
        "The add-a-forecast article lets you pick a start week up to 26 weeks in the past or 104 weeks in the future. The end date cannot pass 130 weeks from the start week. If you type a longer duration, Genesys Cloud reduces it and shows a message. Creation methods on that page are Automatic best method selection, Weighted Historical Index, Weighted Historical Index with Source Data Import, and Import Short-Term Interval Forecast Data.",
        "Automatic best method uses the available historical data, with outlier detection and fixes for missing data. Weighted historical index with source data import uses a CSV instead of system history and allows up to eight source days, such as eight historical Mondays for the forecast Monday. Import Short-Term Interval Forecast Data brings a finished file of at most six weeks, and every row must fall inside the forecast duration or the system returns an error. For Genesys Cloud EX data that is injected from outside, the article says to use Automatic best method: weighted historical index caches conversation data older than one day and permanently excludes data that was not injected yet.",
    ],
    cites("forecast-add", "wfm-forecasts"),
    fig("Pick a method. The short-term import is a finished file, not another weighting.", [
        ("auto", "Automatic", "wem", 16, 28),
        ("wt", "Weighted", "queue", 46, 28),
        ("csv", "Eight days", "architect", 46, 72),
        ("imp", "Import", "agent", 80, 40),
    ], [("auto", "wt"), ("wt", "csv"), ("csv", "imp")]),
    "Match a data source to a method",
    [
        ("History", "Automatic", "Uses available history", "Not a file of eight Mondays.", "EX injections stay on this method"),
        ("Weights", "Weighted index", "System history", "You choose the weighting.", "Different from a finished import"),
        ("File", "Source import", "Up to eight source days", "Mapped onto forecast days.", "Still a weighted method"),
        ("Done", "Short-term import", "At most six weeks", "Rows outside the duration error.", "Not the 130-week outer limit"),
    ],
    [
        q("A forecast start week may be:", "Up to 26 weeks in the past or 104 weeks in the future", ["Only next week", "Up to two years in the past", "Any date, with no outer end"], "The end still cannot pass 130 weeks from the start."),
        q("If the duration would pass 130 weeks from the start, Genesys Cloud:", "Reduces it to the allowed maximum and explains the limit", ["Saves it and schedules the extra weeks", "Converts it to bullseye rings", "Deletes the business unit"], "The add-a-forecast article describes that reduction."),
        q("Weighted historical index with source data import allows:", "Up to eight source days", ["Up to 500 topics", "Up to six rings", "Up to 20 agent-score pairs"], "The example is eight historical Mondays for the forecast Monday."),
        q("Import Short-Term Interval Forecast Data is limited to:", "Six weeks, and every row must sit inside the forecast duration", ["130 weeks of daily data", "Two years", "A single interval"], "Data outside the duration returns an error."),
        q("For Genesys Cloud EX forecasts fed by injected data, the article says to use:", "Automatic best method selection", ["Weighted historical index", "A bullseye skill removal", "Direct routing"], "Weighted historical index can cache older data and exclude injections that have not arrived."),
        q("Automatic best method differs from weighted historical index because:", "It uses the available historical data rather than a chosen index of source days", ["It ignores history", "It only imports a CSV", "It generates a schedule by itself"], "The schedule is a later step. This choice only builds the forecast."),
    ],
    [("Window", "26 weeks back, 104 ahead, 130 from the start."), ("Automatic", "Available history."), ("Eight days", "Source-data import."), ("Six-week file", "Finished short-term import.")],
    "Pick a method for three orgs",
    ["A normal history.", "A spreadsheet of eight Mondays.", "An EX feed that sometimes arrives late.", "The method you will not use for the third."],
    "The late EX feed is automatic best method, not weighted historical index.",
    ("Late injection", "An EX forecast uses weighted historical index, and Mondays that arrive a day late never appear.", "The article says data older than one day is cached and missing injections are excluded.", "The method was copied from a CX org.", "Recreate it with automatic best method selection."),
))

add(lesson(
    "n-editor", "The editor shows history as read-only lines", "Core", 11,
    "Short-term granularity is 15, 30, or 60 minutes. Long-term granularity is daily or weekly.",
    [
        "The forecast editor article puts Short-Term Forecast and Long-Term Forecast on two icons. Short-term granularity choices are 15 minutes, 30 minutes, and 60 minutes. Long-term choices are daily and weekly. Pointing at the graph shows the data for that time. The lines are the historic data used to create the forecast, and they are read-only. Colors match the metrics.",
        "The editor sits below the graph. Dragging selects a smaller date range, and clicking outside the selection clears that zoom. Checkboxes on the left change which metric variables are included. This page does not say that editing a line rewrites history. If you need to change the forecast itself, use the modification controls on the forecast article rather than assuming the historic line is editable.",
    ],
    cites("forecast-editor", "wfm-forecasts"),
    fig("Two icons, two granularities. The historic line does not accept edits.", [
        ("st", "15 30 60", "queue", 28, 36),
        ("lt", "Day Week", "region", 62, 36),
        ("ro", "Read-only", "wem", 84, 70),
    ], [("st", "lt"), ("lt", "ro")]),
    "Read the graph before you change anything",
    [
        ("Icon", "Short-term", "15, 30, or 60 minutes", "One week of intervals lives in the other article.", "This page is the graph"),
        ("Icon", "Long-term", "Daily or weekly", "Seasonality stays here.", "Not a schedule button"),
        ("Line", "History", "Read-only", "Color is the metric.", "Hover for a time"),
        ("Zoom", "Drag", "Then click outside", "That clears the filter.", "Checkboxes pick metrics"),
    ],
    [
        q("Short-term granularities in the editor are:", "15, 30, and 60 minutes", ["Daily and weekly", "2 seconds and 72 hours", "Six rings"], "Daily and weekly are the long-term choices."),
        q("Long-term granularities in the editor are:", "Daily and weekly", ["15 minutes only", "One priority point", "A single interval"], "The article lists those two."),
        q("The lines on the graph are:", "Historic data, and read-only", ["The schedule you can drag", "Agent scores", "SIP responses"], "Colors correspond to metrics."),
        q("A drag on the editor:", "Zooms to a smaller date range", ["Deletes the forecast", "Publishes a flow", "Removes a skill"], "Click outside the selection to clear it."),
        q("Changing history by dragging a line is:", "Not what this article describes", ["The way you set volume", "Required before scheduling", "The same as bullseye option 2"], "Use the forecast article’s modification controls if you need to change forecast values."),
        q("The two views are opened from:", "Icons at the top left of the graph", ["The queue routing tab", "Architect", "The OAuth client"], "Short-term and long-term are separate icons."),
    ],
    [("Short-term", "15, 30, or 60 minutes."), ("Long-term", "Daily or weekly."), ("Lines", "History, read-only."), ("Zoom", "Drag, then click outside.")],
    "Say what you can change",
    ["The granularity.", "The metrics checked on the left.", "The zoom.", "A sentence that the historic line stays read-only."],
    "The historic line is not listed as an edit.",
    ("Repainted history", "An analyst drags last Monday’s line up so the forecast looks busier.", "The editor article says those lines are read-only.", "The zoom gesture was mistaken for an edit.", "Leave the line. Change the forecast through the modification path on the forecast article, then say what you changed."),
))

add(lesson(
    "n-cover", "The schedule has to sit inside the short-term weeks", "Advanced", 13,
    "Generation offers a forecast only when those weeks cover the schedule, and only one schedule is generated at a time.",
    [
        "The schedules article lists three generation choices: create a schedule with a forecast, create one without a forecast, and create a blank schedule. A forecast-based schedule has to use a forecast marked Available for Schedule, and the schedule’s dates have to fall inside that forecast’s short-term weeks. The article’s example: a six-week schedule must align with those six short-term weeks, and a four-week schedule must fall inside a four-, five-, or six-week short-term portion. The generate dialog’s maximum number of weeks is 6.",
        "The generate-from-forecast article says you can generate only one schedule per business unit at a time. The new attempt shows in Last Scheduling Attempts. A schedule without a forecast is a blank pattern of shifts when no forecast exists. It is not a secret use of the long-term view. The forecast article adds the planning rule in front of all of this: if two business units share load, someone has to adjust the forecast by hand, because the product expects a clean split of resources and work.",
    ],
    cites("wfm-schedules", "wfm-from-forecast", "wfm-forecasts"),
    fig("The schedule rectangle has to fit inside the short-term rectangle.", [
        ("f", "Short-term", "wem", 22, 40),
        ("s", "Schedule", "agent", 58, 40),
        ("one", "One at a time", "queue", 86, 40),
    ], [("f", "s"), ("s", "one")]),
    "Check the overlap before you generate",
    [
        ("Flag", "Available for Schedule", "Must be on", "Otherwise the forecast is not listed.", "Long-term weeks do not count"),
        ("Fit", "Dates", "Inside the short-term weeks", "Six must match six.", "Four can use four, five, or six"),
        ("Cap", "Dialog", "At most six weeks", "A longer plan is another forecast.", "Not 130 weeks"),
        ("Unit", "Business unit", "One generation at a time", "Shared load is a manual forecast edit.", "Not a second hidden schedule"),
    ],
    [
        q("A six-week schedule can use a forecast when:", "That forecast’s short-term weeks are those same six weeks", ["The long-term view covers the year", "Any forecast exists", "The queue uses bullseye"], "The schedules article requires the short-term weeks to cover the schedule."),
        q("A four-week schedule may use:", "A four-, five-, or six-week short-term portion that contains it", ["Only a two-year forecast", "Only a blank schedule", "A skill expression filter"], "The weeks have to overlap. Longer short-term portions are allowed."),
        q("The generate dialog’s week maximum is:", "6", ["26", "104", "130"], "26 and 104 are forecast search windows. 130 is the create-page outer limit."),
        q("Forecasts offered in that dialog are:", "Marked Available for Schedule", ["Every forecast in the org", "Only imported CSV files", "Only long-term views"], "Clearing the checkbox hides the forecast."),
        q("How many schedules can one business unit generate at a time?", "One", ["Five", "Six", "One per queue"], "The generate-from-forecast article says the new attempt replaces the display in Last Scheduling Attempts."),
        q("Shared workload across business units is handled by:", "A manual forecast adjustment, because the article wants the load separated", ["Bullseye option 2", "Direct routing", "An automatic merge"], "The forecast article says administrators adjust when the split is not clean."),
    ],
    [("Overlap", "Short-term weeks must cover the schedule."), ("Six", "The generation maximum."), ("One", "Per business unit at a time."), ("Shared load", "Adjust the forecast by hand.")],
    "Accept or reject three generations",
    ["Six-week schedule, six short-term weeks, checkbox on.", "Six-week schedule, long-term view only.", "A second generation started while the first is still running for that business unit.", "The manual step if two business units share the same agents."],
    "Only the first generation matches the articles.",
    ("Double generate", "Two planners generate schedules for the same business unit at the same moment and expect both to stick.", "The article allows one generation at a time.", "The checkbox was mistaken for a lock.", "Wait for the attempt in Last Scheduling Attempts, then generate the next one."),
))

add(lesson(
    "n-use", "Use the forecast, then go back to the floor", "Advanced", 11,
    "Intraday compares the plan with what happened. Adherence is a different WFM page.",
    [
        "The workforce management overview lists developing forecasts and comparing the intraday forecast with actual values, next to blank schedules, forecast-based schedules, and schedules without a forecast. The comparison is how you notice that Tuesday’s interval was wrong. It does not rewrite the historic line in the editor, and it does not change who ACD offers.",
        "Adherence, time off, and the business-unit structure stay on the WFM track. Quality forms and speech programs stay on the quality chapter. A forecast that cannot explain an abandon rate is not a broken bullseye ring. Say which system you are looking at before you change a skill, a ring, or a schedule.",
    ],
    cites("wfm-overview", "wfm-forecasts", "wem"),
    fig("Intraday is forecast versus actual. The queue is a different picture.", [
        ("plan", "Forecast", "wem", 18, 40),
        ("now", "Actual", "agent", 50, 40),
        ("q", "Queue", "queue", 82, 40),
    ], [("plan", "now")]),
    "Choose the page that can answer",
    [
        ("Interval", "Intraday", "Forecast versus actual", "The overview names that comparison.", "Not a routing trace"),
        ("Shift", "Schedule", "Short-term weeks", "Or blank, or without a forecast.", "One generation at a time"),
        ("Offer", "Queue", "Routing method", "Skills and rings live there.", "A forecast will not alert an agent"),
        ("Listen", "Quality", "A later chapter", "Forms and topics.", "Not a staffing grid"),
    ],
    [
        q("Intraday, the overview asks you to compare:", "The forecast and the actual values", ["Two OAuth grants", "Bullseye rings", "Exam codes"], "That comparison is named on the workforce management overview."),
        q("A wrong Tuesday interval means you start with:", "The forecast and the intraday comparison", ["A new SIP trunk", "A direct-routing API", "A topic phrase"], "The queue is the next place only if the offer itself is wrong."),
        q("The editor’s historic lines, while you do that comparison, are:", "Still read-only", ["The actual values you type", "The schedule", "The evaluation form"], "The editor article says the lines are read-only."),
        q("Adherence belongs in:", "The WFM track", ["The skill expression filter", "The Salesforce embed", "RFC 3261"], "This chapter does not replace that track."),
        q("A forecast cannot:", "Alert an agent", ["Describe offered volume", "Feed a short-term schedule", "Show a long-term season"], "Alerting is ACD."),
        q("Schedules without a forecast are:", "A documented generation choice for a shift pattern", ["The long-term view in disguise", "Prohibited", "A bullseye option"], "The schedules article lists that choice beside the forecast-based one."),
    ],
    [("Intraday", "Forecast versus actual."), ("Read-only", "Historic graph lines."), ("Adherence", "WFM track."), ("Alert", "Still the queue.")],
    "Route four complaints",
    ["Tuesday was busier than the interval.", "Agents were off the schedule.", "The wrong skill was offered.", "Nobody was evaluated.", "Name the chapter for each."],
    "Only the first complaint starts in this chapter.",
    ("One screen", "The forecast is edited to remove a skill because abandon rose.", "Abandon and skills are queue routing. The forecast plans volume and handle time.", "The pictures were stacked.", "Leave the forecast. Open the queue method, then come back if the interval itself was wrong."),
))
