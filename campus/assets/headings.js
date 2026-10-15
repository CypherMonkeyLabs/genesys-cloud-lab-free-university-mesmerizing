/** Track and lesson headings only. Lesson bodies stay English. */
const HEADS = {
  "foundations": {
    "es": "Fundamentos",
    "hi": "आधार",
    "te": "పునాదులు",
    "fr": "Fondations",
    "de": "Grundlagen",
    "ja": "基礎",
    "ar": "الأساسات"
  },
  "f-platform": {
    "es": "Qué es Genesys Cloud CX",
    "hi": "Genesys Cloud CX क्या है",
    "te": "Genesys Cloud CX అంటే ఏమిటి",
    "fr": "Qu’est-ce que Genesys Cloud CX",
    "de": "Was Genesys Cloud CX ist",
    "ja": "Genesys Cloud CX とは",
    "ar": "ما هو Genesys Cloud CX"
  },
  "f-regions": {
    "es": "Regiones núcleo y medios satélite",
    "hi": "कोर क्षेत्र और सैटेलाइट मीडिया",
    "te": "కోర్ ప్రాంతాలు మరియు శాటిలైట్ మీడియా",
    "fr": "Régions cœur et média satellite",
    "de": "Kernregionen und Satellitenmedien",
    "ja": "コアリジョンとサテライトメディア",
    "ar": "المناطق الأساسية والوسائط الساتلية"
  },
  "f-sip": {
    "es": "SIP, RTP y lo que hace el troncal",
    "hi": "SIP, RTP और ट्रंक क्या कर रहा है",
    "te": "SIP, RTP మరియు ట్రంక్ ఏమి చేస్తోంది",
    "fr": "SIP, RTP et ce que fait le trunk",
    "de": "SIP, RTP und was der Trunk tut",
    "ja": "SIP、RTP、トランクの役割",
    "ar": "SIP وRTP وما يفعله الجذع"
  },
  "f-acd-idea": {
    "es": "Qué es ACD antes de nombrar una cola",
    "hi": "क्यू का नाम रखने से पहले ACD क्या है",
    "te": "క్యూ పేరు పెట్టే ముందు ACD అంటే ఏమిటి",
    "fr": "Ce qu’est l’ACD avant de nommer une file",
    "de": "Was ACD ist, bevor eine Queue einen Namen hat",
    "ja": "キューに名前を付ける前の ACD",
    "ar": "ما هو ACD قبل تسمية قائمة الانتظار"
  },
  "f-digital": {
    "es": "Conversaciones digitales junto a la voz",
    "hi": "आवाज़ के साथ डिजिटल बातचीत",
    "te": "వాయిస్ పక్కన డిజిటల్ సంభాషణలు",
    "fr": "Conversations numériques à côté de la voix",
    "de": "Digitale Gespräche neben Sprache",
    "ja": "音声のそばのデジタル会話",
    "ar": "محادثات رقمية إلى جانب الصوت"
  },
  "f-access": {
    "es": "Divisiones, antes de que los roles se compliquen",
    "hi": "भूमिकाएँ जटिल होने से पहले डिवीजन",
    "te": "పాత్రలు క్లిష్టం కాకముందే డివిజన్లు",
    "fr": "Les divisions, avant que les rôles se compliquent",
    "de": "Divisionen, bevor Rollen kompliziert werden",
    "ja": "ロールが複雑になる前のディビジョン",
    "ar": "الأقسام قبل أن تتعقّد الأدوار"
  },
  "f-read": {
    "es": "Cómo leer una página de Genesys sin inventar el resto",
    "hi": "बाकी गढ़े बिना Genesys पेज कैसे पढ़ें",
    "te": "మిగతా దాన్ని కల్పించకుండా Genesys పేజీని ఎలా చదవాలి",
    "fr": "Lire une page Genesys sans inventer le reste",
    "de": "Eine Genesys-Seite lesen, ohne den Rest zu erfinden",
    "ja": "残りを創作せずに Genesys のページを読む",
    "ar": "كيف تقرأ صفحة Genesys دون اختراع الباقي"
  },
  "f-prereq": {
    "es": "Requisitos antes del primer troncal",
    "hi": "पहले ट्रंक से पहले की शर्तें",
    "te": "మొదటి ట్రంక్‌కు ముందు అవసరాలు",
    "fr": "Prérequis avant le premier trunk",
    "de": "Voraussetzungen vor dem ersten Trunk",
    "ja": "最初のトランクの前の前提",
    "ar": "المتطلبات قبل أول جذع"
  },
  "org": {
    "es": "Organización y licencias",
    "hi": "संगठन और लाइसेंस",
    "te": "సంస్థ మరియు లైసెన్సులు",
    "fr": "Organisation et licences",
    "de": "Organisation und Lizenzen",
    "ja": "組織とライセンス",
    "ar": "المؤسسة والتراخيص"
  },
  "o-place": {
    "es": "Coloca la organización en una región núcleo",
    "hi": "संगठन को एक कोर क्षेत्र में रखें",
    "te": "సంస్థను ఒక కోర్ ప్రాంతంలో ఉంచండి",
    "fr": "Placez l’organisation dans une région cœur",
    "de": "Die Organisation in eine Kernregion legen",
    "ja": "組織をコアリジョンに置く",
    "ar": "ضع المؤسسة في منطقة أساسية"
  },
  "o-roles": {
    "es": "Los roles son listas de permisos emparejadas con divisiones",
    "hi": "भूमिकाएँ डिवीजनों के साथ जोड़ी गई अनुमति सूचियाँ हैं",
    "te": "పాత్రలు డివిజన్లతో జత చేసిన అనుమతి జాబితాలు",
    "fr": "Les rôles sont des listes de droits liées aux divisions",
    "de": "Rollen sind Berechtigungslisten, gepaart mit Divisionen",
    "ja": "ロールはディビジョンと組になった権限リスト",
    "ar": "الأدوار قوائم أذونات مقترنة بالأقسام"
  },
  "o-concurrent": {
    "es": "Licencias nombradas y el pico concurrente",
    "hi": "नामित लाइसेंस और समवर्ती शिखर",
    "te": "పేరున్న లైసెన్సులు మరియు ఏకకాల శిఖరం",
    "fr": "Licences nommées et le pic simultané",
    "de": "Benannte Lizenzen und die gleichzeitige Spitze",
    "ja": "名前付きライセンスと同時ピーク",
    "ar": "التراخيص المسماة وذروة التزامن"
  },
  "o-packages": {
    "es": "Elige CX 1, CX 2, CX 3 o CX 4 a propósito",
    "hi": "जानबूझकर CX 1, CX 2, CX 3 या CX 4 चुनें",
    "te": "ఉద్దేశపూర్వకంగా CX 1, CX 2, CX 3 లేదా CX 4 ఎంచుకోండి",
    "fr": "Choisissez CX 1, CX 2, CX 3 ou CX 4 exprès",
    "de": "CX 1, CX 2, CX 3 oder CX 4 bewusst wählen",
    "ja": "CX 1、CX 2、CX 3、CX 4 を意図して選ぶ",
    "ar": "اختر CX 1 أو CX 2 أو CX 3 أو CX 4 عن قصد"
  },
  "o-people": {
    "es": "Personas, colas y la línea de 5.000 miembros",
    "hi": "लोग, क्यू और 5,000 सदस्य की सीमा",
    "te": "వ్యక్తులు, క్యూలు మరియు 5,000 సభ్యుల పరిమితి",
    "fr": "Personnes, files et la limite de 5 000 membres",
    "de": "Personen, Queues und die Grenze von 5.000 Mitgliedern",
    "ja": "人とキューと 5,000 人の上限",
    "ar": "الأشخاص وقوائم الانتظار وحدّ 5,000 عضو"
  },
  "o-fair": {
    "es": "El uso justo es un fondo, no una factura misteriosa",
    "hi": "फेयर यूज़ एक पूल है, रहस्यमय बिल नहीं",
    "te": "ఫెయిర్ యూజ్ ఒక పూల్, రహస్య బిల్లు కాదు",
    "fr": "L’usage équitable est un pool, pas une facture mystère",
    "de": "Fair Use ist ein Pool, keine rätselhafte Rechnung",
    "ja": "フェアユースは謎の請求書ではなくプール",
    "ar": "الاستخدام العادل رصيد مشترك وليس فاتورة غامضة"
  },
  "o-bootstrap": {
    "es": "Lista de administración de la primera semana",
    "hi": "पहले सप्ताह की व्यवस्थापक जाँच सूची",
    "te": "మొదటి వారం నిర్వాహక చెక్‌లిస్ట్",
    "fr": "Liste d’admin pour la première semaine",
    "de": "Admin-Checkliste der ersten Woche",
    "ja": "最初の週の管理チェックリスト",
    "ar": "قائمة إدارة الأسبوع الأول"
  },
  "architect": {
    "es": "Flujos de Architect",
    "hi": "आर्किटेक्ट फ़्लो",
    "te": "ఆర్కిటెక్ట్ ఫ్లోలు",
    "fr": "Flux Architect",
    "de": "Architect-Flows",
    "ja": "Architect フロー",
    "ar": "تدفقات Architect"
  },
  "a-types": {
    "es": "Los tipos de flujo en la página de inicio de Architect",
    "hi": "Architect होम पेज पर फ़्लो प्रकार",
    "te": "Architect హోమ్ పేజీలోని ఫ్లో రకాలు",
    "fr": "Les types de flux sur l’accueil Architect",
    "de": "Die Flow-Typen auf der Architect-Startseite",
    "ja": "Architect ホームのフロー種別",
    "ar": "أنواع التدفق في صفحة Architect الرئيسية"
  },
  "a-task": {
    "es": "Tareas, menús y una salida",
    "hi": "कार्य, मेनू और बाहर निकलने का रास्ता",
    "te": "టాస్క్‌లు, మెనూలు మరియు బయటకు దారి",
    "fr": "Tâches, menus et une sortie",
    "de": "Aufgaben, Menüs und ein Ausweg",
    "ja": "タスク、メニュー、出口",
    "ar": "المهام والقوائم ومخرج"
  },
  "a-inqueue": {
    "es": "Los flujos en cola son la experiencia de espera",
    "hi": "इन-क्यू फ़्लो प्रतीक्षा का अनुभव हैं",
    "te": "ఇన్-క్యూ ఫ్లోలు వేచి ఉండే అనుభవం",
    "fr": "Les flux en file sont l’attente",
    "de": "In-Queue-Flows sind das Warteerlebnis",
    "ja": "インキューフローは待機体験",
    "ar": "تدفقات الانتظار هي تجربة التعليق"
  },
  "a-data": {
    "es": "Acciones de datos y datos del participante",
    "hi": "डेटा क्रियाएँ और प्रतिभागी डेटा",
    "te": "డేటా చర్యలు మరియు పాల్గొనేవారి డేటా",
    "fr": "Actions de données et données du participant",
    "de": "Datenaktionen und Teilnehmerdaten",
    "ja": "データアクションと参加者データ",
    "ar": "إجراءات البيانات وبيانات المشارك"
  },
  "a-common": {
    "es": "Los módulos comunes evitan copiar tareas",
    "hi": "कॉमन मॉड्यूल कार्यों की नकल रोकते हैं",
    "te": "కామన్ మాడ్యూల్స్ టాస్క్‌లను కాపీ చేయడం ఆపుతాయి",
    "fr": "Les modules communs évitent de copier les tâches",
    "de": "Gemeinsame Module stoppen das Kopieren von Aufgaben",
    "ja": "共通モジュールはタスクの複製を止める",
    "ar": "الوحدات المشتركة توقف نسخ المهام"
  },
  "a-secure": {
    "es": "Los flujos seguros alejan los dígitos de la grabación",
    "hi": "सुरक्षित कॉल फ़्लो अंकों को रिकॉर्डिंग से दूर रखते हैं",
    "te": "సురక్షిత కాల్ ఫ్లోలు అంకెలను రికార్డింగ్ నుండి దూరంగా ఉంచుతాయి",
    "fr": "Les flux sécurisés éloignent les chiffres de l’enregistrement",
    "de": "Sichere Anrufflows halten Ziffern von der Aufnahme fern",
    "ja": "セキュアコールフローは数字を録音から離す",
    "ar": "تدفقات الاتصال الآمنة تُبعد الأرقام عن التسجيل"
  },
  "a-botcall": {
    "es": "Llama a un bot desde el flujo de entrada",
    "hi": "इनबाउंड फ़्लो से बॉट को कॉल करें",
    "te": "ఇన్‌బౌండ్ ఫ్లో నుండి బాట్‌ను పిలవండి",
    "fr": "Appeler un bot depuis le flux entrant",
    "de": "Einen Bot aus dem Inbound-Flow anrufen",
    "ja": "着信フローからボットを呼ぶ",
    "ar": "استدعِ روبوتاً من تدفق الوارد"
  },
  "a-publish": {
    "es": "Publicar, división e información del flujo",
    "hi": "प्रकाशित करें, डिवीजन और फ़्लो इनसाइट्स",
    "te": "ప్రచురించండి, డివిజన్ మరియు ఫ్లో ఇన్‌సైట్స్",
    "fr": "Publier, division et Flow Insights",
    "de": "Veröffentlichen, Division und Flow Insights",
    "ja": "公開、ディビジョン、Flow Insights",
    "ar": "النشر والقسم ورؤى التدفق"
  },
  "acd": {
    "es": "Enrutamiento ACD",
    "hi": "एसीडी रूटिंग",
    "te": "ఏసీడీ రూటింగ్",
    "fr": "Routage ACD",
    "de": "ACD-Routing",
    "ja": "ACD ルーティング",
    "ar": "توجيه ACD"
  },
  "r-methods": {
    "es": "Cinco métodos de enrutamiento",
    "hi": "पाँच रूटिंग विधियाँ",
    "te": "ఐదు రూటింగ్ పద్ధతులు",
    "fr": "Cinq méthodes de routage",
    "de": "Fünf Routing-Methoden",
    "ja": "5 つのルーティング方式",
    "ar": "خمس طرق للتوجيه"
  },
  "r-eval": {
    "es": "Todas las habilidades, el mejor disponible o ignorar",
    "hi": "सभी कौशल, सर्वोत्तम उपलब्ध, या अनदेखा",
    "te": "అన్ని నైపుణ్యాలు, అందుబాటులో ఉన్న ఉత్తమం, లేదా విస్మరించు",
    "fr": "Toutes les compétences, le meilleur disponible, ou ignorer",
    "de": "Alle Skills, bester Verfügbarer oder ignorieren",
    "ja": "全スキル、最善の空き、または無視",
    "ar": "كل المهارات أو الأفضل المتاح أو التجاهل"
  },
  "r-score": {
    "es": "Puntuación de conversación y de prioridad",
    "hi": "वार्तालाप स्कोर और प्राथमिकता स्कोर",
    "te": "సంభాషణ స్కోర్ మరియు ప్రాధాన్యత స్కోర్",
    "fr": "Score de conversation et score de priorité",
    "de": "Gesprächswert und Prioritätswert",
    "ja": "会話スコアと優先度スコア",
    "ar": "درجة المحادثة ودرجة الأولوية"
  },
  "r-bullseye": {
    "es": "Los anillos bullseye amplían el objetivo",
    "hi": "बुलआई रिंग लक्ष्य को चौड़ा करते हैं",
    "te": "బుల్స్‌ఐ రింగ్‌లు లక్ష్యాన్ని విస్తరిస్తాయి",
    "fr": "Les anneaux bullseye élargissent la cible",
    "de": "Bullseye-Ringe weiten das Ziel",
    "ja": "ブルズアイの輪が対象を広げる",
    "ar": "حلقات بولزآي توسّع الهدف"
  },
  "r-preferred": {
    "es": "Los agentes preferidos se prueban primero",
    "hi": "पसंदीदा एजेंट पहले आज़माए जाते हैं",
    "te": "ఇష్టమైన ఏజెంట్లను ముందు ప్రయత్నిస్తారు",
    "fr": "Les agents préférés sont essayés d’abord",
    "de": "Bevorzugte Agenten werden zuerst versucht",
    "ja": "優先エージェントを先に試す",
    "ar": "يُجرَّب الوكلاء المفضّلون أولاً"
  },
  "r-predict": {
    "es": "El enrutamiento predictivo es un modelo de KPI con tiempo límite",
    "hi": "प्रेडिक्टिव रूटिंग समय सीमा वाला KPI मॉडल है",
    "te": "ప్రిడిక్టివ్ రూటింగ్ గడువుతో కూడిన KPI నమూనా",
    "fr": "Le routage prédictif est un modèle de KPI avec délai",
    "de": "Predictive Routing ist ein KPI-Modell mit Zeitlimit",
    "ja": "プレディクティブルーティングは期限付き KPI モデル",
    "ar": "التوجيه التنبؤي نموذج مؤشر بأجل"
  },
  "r-conditional": {
    "es": "El enrutamiento condicional de grupos pide agentes con cuidado",
    "hi": "सशर्त समूह रूटिंग एजेंटों को सावधानी से माँगता है",
    "te": "కండిషనల్ గ్రూప్ రూటింగ్ ఏజెంట్లను జాగ్రత్తగా అడుగుతుంది",
    "fr": "Le routage conditionnel de groupe emprunte des agents avec soin",
    "de": "Bedingtes Gruppenrouting leiht Agenten vorsichtig",
    "ja": "条件付きグループルーティングは慎重に担当者を借りる",
    "ar": "توجيه المجموعة المشروط يستعير الوكلاء بحذر"
  },
  "r-util": {
    "es": "Utilización y No responde",
    "hi": "उपयोग और जवाब नहीं",
    "te": "వినియోగం మరియు స్పందించడం లేదు",
    "fr": "Utilisation et Non-réponse",
    "de": "Auslastung und Keine Antwort",
    "ja": "稼働率と応答なし",
    "ar": "الاستخدام وعدم الرد"
  },
  "queues": {
    "es": "Colas, habilidades y cierre",
    "hi": "क्यू, कौशल और रैप-अप",
    "te": "క్యూలు, నైపుణ్యాలు మరియు ర్యాప్-అప్",
    "fr": "Files, compétences et clôture",
    "de": "Queues, Skills und Wrap-up",
    "ja": "キュー、スキル、ラップアップ",
    "ar": "قوائم الانتظار والمهارات والإنهاء"
  },
  "q-create": {
    "es": "Crea la cola en una división",
    "hi": "एक डिवीजन में क्यू बनाएँ",
    "te": "ఒక డివిజన్‌లో క్యూ సృష్టించండి",
    "fr": "Créez la file dans une division",
    "de": "Die Queue in einer Division anlegen",
    "ja": "ディビジョンにキューを作る",
    "ar": "أنشئ قائمة الانتظار في قسم"
  },
  "q-skills": {
    "es": "Las habilidades y la competencia están en el agente",
    "hi": "कौशल और दक्षता एजेंट पर हैं",
    "te": "నైపుణ్యాలు మరియు ప్రావీణ్యం ఏజెంట్‌పై ఉంటాయి",
    "fr": "Compétences et niveau sont sur l’agent",
    "de": "Skills und Können liegen beim Agenten",
    "ja": "スキルと熟練度はエージェント側",
    "ar": "المهارات والإتقان على الوكيل"
  },
  "q-acw": {
    "es": "El trabajo posterior y los códigos de cierre del sistema",
    "hi": "कॉल के बाद का काम और सिस्टम रैप-अप कोड",
    "te": "కాల్ తర్వాత పని మరియు సిస్టమ్ ర్యాప్-అప్ కోడ్‌లు",
    "fr": "Le travail après appel et les codes système",
    "de": "Nachbearbeitung und System-Wrap-up-Codes",
    "ja": "後処理とシステムのラップアップコード",
    "ar": "عمل ما بعد الاتصال ورموز الإنهاء في النظام"
  },
  "q-wrapdiv": {
    "es": "Los códigos de cierre también viven en divisiones",
    "hi": "रैप-अप कोड भी डिवीजनों में रहते हैं",
    "te": "ర్యాప్-అప్ కోడ్‌లు కూడా డివిజన్లలో ఉంటాయి",
    "fr": "Les codes de clôture vivent aussi dans les divisions",
    "de": "Wrap-up-Codes leben auch in Divisionen",
    "ja": "ラップアップコードもディビジョンにある",
    "ar": "رموز الإنهاء تعيش أيضاً في الأقسام"
  },
  "q-sl": {
    "es": "El nivel de servicio es un porcentaje y un objetivo en segundos",
    "hi": "सेवा स्तर एक प्रतिशत और सेकंड में लक्ष्य है",
    "te": "సేవా స్థాయి ఒక శాతం మరియు సెకన్లలో లక్ష్యం",
    "fr": "Le niveau de service est un pourcentage et une cible en secondes",
    "de": "Servicelevel ist ein Prozentwert und ein Ziel in Sekunden",
    "ja": "サービスレベルは割合と秒の目標",
    "ar": "مستوى الخدمة نسبة وهدف بالثواني"
  },
  "q-callback": {
    "es": "Las devoluciones de llamada son interacciones con sus propias reglas",
    "hi": "कॉलबैक अपनी नियमों वाली बातचीत हैं",
    "te": "కాల్‌బ్యాక్‌లు సొంత నియమాలున్న పరస్పర చర్యలు",
    "fr": "Les rappels sont des interactions avec leurs règles",
    "de": "Rückrufe sind Interaktionen mit eigenen Regeln",
    "ja": "コールバックは独自ルールのインタラクション",
    "ar": "معاودة الاتصال تفاعلات بقواعدها"
  },
  "q-members": {
    "es": "Pertenencia, En cola y la trampa de copiar",
    "hi": "सदस्यता, ऑन क्यू और कॉपी का जाल",
    "te": "సభ్యత్వం, ఆన్ క్యూ మరియు కాపీ ఉచ్చు",
    "fr": "Appartenance, En file et le piège de la copie",
    "de": "Mitgliedschaft, On Queue und die Kopierfalle",
    "ja": "所属、オンキュー、コピーの罠",
    "ar": "العضوية وعلى قائمة الانتظار وفخ النسخ"
  },
  "byoc": {
    "es": "BYOC Cloud y troncales SIP",
    "hi": "BYOC Cloud और SIP ट्रंक",
    "te": "BYOC Cloud మరియు SIP ట్రంక్‌లు",
    "fr": "BYOC Cloud et trunks SIP",
    "de": "BYOC Cloud und SIP-Trunks",
    "ja": "BYOC Cloud と SIP トランク",
    "ar": "BYOC Cloud وجذوع SIP"
  },
  "b-what": {
    "es": "BYOC Cloud es tu operador y el medio de Genesys",
    "hi": "BYOC Cloud आपका कैरियर है, Genesys का मीडिया",
    "te": "BYOC Cloud మీ క్యారియర్, Genesys మీడియా",
    "fr": "BYOC Cloud, c’est votre opérateur et le média de Genesys",
    "de": "BYOC Cloud ist Ihr Carrier, Genesys das Medium",
    "ja": "BYOC Cloud はあなたの事業者、メディアは Genesys",
    "ar": "BYOC Cloud ناقلُك ووسائط Genesys"
  },
  "b-types": {
    "es": "Troncales de operador y troncales de PBX",
    "hi": "कैरियर ट्रंक और PBX ट्रंक",
    "te": "క్యారియర్ ట్రంక్‌లు మరియు PBX ట్రంక్‌లు",
    "fr": "Trunks opérateur et trunks PBX",
    "de": "Carrier-Trunks und PBX-Trunks",
    "ja": "キャリアトランクと PBX トランク",
    "ar": "جذوع الناقل وجذوع PBX"
  },
  "b-order": {
    "es": "El orden de la guía rápida",
    "hi": "त्वरित-प्रारंभ का क्रम",
    "te": "త్వరిత ప్రారంభ క్రమం",
    "fr": "L’ordre du démarrage rapide",
    "de": "Die Reihenfolge des Schnellstarts",
    "ja": "クイックスタートの順序",
    "ar": "ترتيب البدء السريع"
  },
  "b-dcvp": {
    "es": "Dynamic Cloud Voice es la plataforma actual",
    "hi": "डायनेमिक क्लाउड वॉइस वर्तमान प्लेटफ़ॉर्म है",
    "te": "డైనమిక్ క్లౌడ్ వాయిస్ ప్రస్తుత వేదిక",
    "fr": "Dynamic Cloud Voice est la plateforme actuelle",
    "de": "Dynamic Cloud Voice ist die aktuelle Plattform",
    "ja": "Dynamic Cloud Voice が現在の基盤",
    "ar": "Dynamic Cloud Voice هي المنصة الحالية"
  },
  "b-plans": {
    "es": "Los planes de numeración clasifican lo que se marca",
    "hi": "नंबर प्लान बताते हैं लोग क्या डायल करते हैं",
    "te": "నంబర్ ప్లాన్‌లు ప్రజలు ఏమి డయల్ చేస్తారో వర్గీకరిస్తాయి",
    "fr": "Les plans de numérotation classent ce qu’on compose",
    "de": "Nummernpläne ordnen, was gewählt wird",
    "ja": "番号計画はダイヤル内容を分類する",
    "ar": "خطط الأرقام تصنّف ما يُطلب"
  },
  "b-monitor": {
    "es": "Observa el troncal, no solo el flujo",
    "hi": "केवल फ़्लो नहीं, ट्रंक देखें",
    "te": "ఫ్లో మాత్రమే కాదు, ట్రంక్‌ను చూడండి",
    "fr": "Surveillez le trunk, pas seulement le flux",
    "de": "Den Trunk beobachten, nicht nur den Flow",
    "ja": "フローだけでなくトランクを見る",
    "ar": "راقب الجذع وليس التدفق وحده"
  },
  "b-gcv": {
    "es": "Genesys Cloud Voice es la otra puerta",
    "hi": "Genesys Cloud Voice दूसरा द्वार है",
    "te": "Genesys Cloud Voice మరో తలుపు",
    "fr": "Genesys Cloud Voice est l’autre porte",
    "de": "Genesys Cloud Voice ist die andere Tür",
    "ja": "Genesys Cloud Voice はもう一つの扉",
    "ar": "Genesys Cloud Voice هو الباب الآخر"
  },
  "edge": {
    "es": "El Edge y BYOC Premises",
    "hi": "Edge और BYOC Premises",
    "te": "Edge మరియు BYOC Premises",
    "fr": "L’Edge et BYOC Premises",
    "de": "Der Edge und BYOC Premises",
    "ja": "Edge と BYOC Premises",
    "ar": "جهاز Edge و BYOC Premises"
  },
  "e-role": {
    "es": "El Edge local es el salto de medios en el sitio",
    "hi": "प्रिमाइसेस Edge स्थानीय मीडिया हॉप है",
    "te": "ప్రిమైసెస్ Edge స్థానిక మీడియా హాప్",
    "fr": "L’Edge sur site est le saut média local",
    "de": "Der Premises-Edge ist der lokale Mediensprung",
    "ja": "構内 Edge はローカルなメディアの中継",
    "ar": "Edge المحلي هو قفزة الوسائط في الموقع"
  },
  "e-site": {
    "es": "El enrutamiento del sitio se queda en casa hasta que no puede",
    "hi": "स्थानीय साइट रूटिंग घर पर रहती है जब तक रह सके",
    "te": "స్థానిక సైట్ రూటింగ్ వీలైనంత ఇంట్లోనే ఉంటుంది",
    "fr": "Le routage de site reste chez soi tant qu’il peut",
    "de": "Lokales Site-Routing bleibt daheim, bis es nicht mehr kann",
    "ja": "ローカルサイトの経路は可能な限り拠点に残る",
    "ar": "توجيه الموقع المحلي يبقى في المكان حتى يعجز"
  },
  "e-phone": {
    "es": "Troncales de teléfono, WebRTC y herencia",
    "hi": "फ़ोन ट्रंक, WebRTC और इनहेरिट",
    "te": "ఫోన్ ట్రంక్‌లు, WebRTC మరియు ఇన్‌హెరిట్",
    "fr": "Trunks téléphoniques, WebRTC et héritage",
    "de": "Telefon-Trunks, WebRTC und Vererbung",
    "ja": "電話トランク、WebRTC、継承",
    "ar": "جذوع الهاتف و WebRTC والوراثة"
  },
  "e-fail": {
    "es": "Cuando el Edge local está fuera de línea",
    "hi": "जब स्थानीय Edge ऑफ़लाइन हो",
    "te": "స్థానిక Edge ఆఫ్‌లైన్‌లో ఉన్నప్పుడు",
    "fr": "Quand l’Edge local est hors ligne",
    "de": "Wenn der lokale Edge offline ist",
    "ja": "ローカル Edge がオフラインのとき",
    "ar": "عندما يكون Edge المحلي غير متصل"
  },
  "e-compare": {
    "es": "Elige Cloud, Premises o ambos",
    "hi": "Cloud, Premises या दोनों चुनें",
    "te": "క్లౌడ్, ప్రిమైసెస్ లేదా రెండూ ఎంచుకోండి",
    "fr": "Choisissez Cloud, Premises ou les deux",
    "de": "Cloud, Premises oder beides wählen",
    "ja": "Cloud、Premises、または両方を選ぶ",
    "ar": "اختر السحابة أو الموقع أو كليهما"
  },
  "e-webrtc-net": {
    "es": "Un teléfono en el navegador sigue siendo un extremo de red",
    "hi": "ब्राउज़र फ़ोन फिर भी एक नेटवर्क अंत है",
    "te": "బ్రౌజర్ ఫోన్ ఇంకా నెట్‌వర్క్ అంత్యం",
    "fr": "Un téléphone navigateur reste un point réseau",
    "de": "Ein Browsertelefon bleibt ein Netzendpunkt",
    "ja": "ブラウザ電話もネットワーク端点",
    "ar": "هاتف المتصفح ما زال طرف شبكة"
  },
  "e-checklist": {
    "es": "Lista de puesta en marcha en local",
    "hi": "प्रिमाइसेस चालू करने की जाँच सूची",
    "te": "ప్రిమైసెస్ ప్రారంభ చెక్‌లిస్ట్",
    "fr": "Liste de mise en service sur site",
    "de": "Checkliste für die Inbetriebnahme vor Ort",
    "ja": "構内立ち上げのチェックリスト",
    "ar": "قائمة تشغيل الموقع"
  },
  "emergency": {
    "es": "Números y llamadas de emergencia",
    "hi": "नंबर और आपातकालीन कॉल",
    "te": "నంబర్లు మరియు అత్యవసర కాల్‌లు",
    "fr": "Numéros et appels d’urgence",
    "de": "Nummern und Notrufe",
    "ja": "番号と緊急通話",
    "ar": "الأرقام واتصالات الطوارئ"
  },
  "n-owner": {
    "es": "Nombra al responsable de emergencias antes del DID",
    "hi": "DID से पहले आपात स्वामी का नाम रखें",
    "te": "DID కంటే ముందు అత్యవసర యజమానిని పేర్కొనండి",
    "fr": "Nommez le responsable d’urgence avant le DID",
    "de": "Den Notfallverantwortlichen vor der DID benennen",
    "ja": "DID の前に緊急の責任者を名指す",
    "ar": "سمِّ مسؤول الطوارئ قبل رقم DID"
  },
  "n-plan": {
    "es": "La emergencia es una clasificación y una ruta",
    "hi": "आपात एक वर्गीकरण और एक मार्ग है",
    "te": "అత్యవసరం ఒక వర్గీకరణ మరియు ఒక మార్గం",
    "fr": "L’urgence est une classe et une route",
    "de": "Notfall ist eine Klasse und eine Route",
    "ja": "緊急は分類であり経路",
    "ar": "الطوارئ تصنيف ومسار"
  },
  "n-location": {
    "es": "La ubicación es un lugar físico",
    "hi": "स्थान एक भौतिक जगह है",
    "te": "స్థానం ఒక భౌతిక ప్రదేశం",
    "fr": "L’emplacement est un lieu physique",
    "de": "Der Standort ist ein physischer Ort",
    "ja": "ロケーションは物理的な場所",
    "ar": "الموقع مكان فعلي"
  },
  "n-gcv-limits": {
    "es": "La cobertura de voz es una tabla, no una promesa",
    "hi": "वॉइस कवरेज एक तालिका है, वादा नहीं",
    "te": "వాయిస్ కవరేజ్ ఒక పట్టిక, వాగ్దానం కాదు",
    "fr": "La couverture voix est un tableau, pas une promesse",
    "de": "Sprachabdeckung ist eine Tabelle, kein Versprechen",
    "ja": "音声カバーは表であり約束ではない",
    "ar": "تغطية الصوت جدول وليست وعداً"
  },
  "n-e164": {
    "es": "Normaliza hacia E.164 a propósito",
    "hi": "जानबूझकर E.164 की ओर सामान्य करें",
    "te": "ఉద్దేశపూర్వకంగా E.164 వైపు సాధారణీకరించండి",
    "fr": "Normalisez vers E.164 exprès",
    "de": "Absichtlich Richtung E.164 normalisieren",
    "ja": "意図して E.164 へ正規化する",
    "ar": "طبّع نحو E.164 عن قصد"
  },
  "n-test": {
    "es": "Prueba la emergencia como un cambio, no como una demo",
    "hi": "आपात को डेमो नहीं, बदलाव की तरह जाँचें",
    "te": "అత్యవసరాన్ని డెమోలా కాక మార్పులా పరీక్షించండి",
    "fr": "Testez l’urgence comme un changement, pas une démo",
    "de": "Notfall wie eine Änderung testen, nicht wie eine Demo",
    "ja": "緊急はデモではなく変更として試す",
    "ar": "اختبر الطوارئ كتغيير لا كعرض"
  },
  "wfm": {
    "es": "Gestión de la fuerza de trabajo",
    "hi": "कार्यबल प्रबंधन",
    "te": "కార్యబల నిర్వహణ",
    "fr": "Gestion des effectifs",
    "de": "Workforce Management",
    "ja": "ワークフォース管理",
    "ar": "إدارة القوى العاملة"
  },
  "w-map": {
    "es": "WEM es un conjunto de productos y WFM es uno de ellos",
    "hi": "WEM उत्पादों का समूह है और WFM उनमें से एक है",
    "te": "WEM ఉత్పత్తుల సమూహం, WFM వాటిలో ఒకటి",
    "fr": "WEM est un ensemble de produits, WFM en est un",
    "de": "WEM ist eine Produktfamilie, WFM ist eines davon",
    "ja": "WEM は製品群で、WFM はその一つ",
    "ar": "WEM مجموعة منتجات و WFM أحدها"
  },
  "w-bu": {
    "es": "Unidades de negocio y unidades de gestión",
    "hi": "बिज़नेस यूनिट और मैनेजमेंट यूनिट",
    "te": "బిజినెస్ యూనిట్లు మరియు మేనేజ్‌మెంట్ యూనిట్లు",
    "fr": "Unités commerciales et unités de gestion",
    "de": "Geschäftseinheiten und Managementeinheiten",
    "ja": "ビジネスユニットと管理ユニット",
    "ar": "وحدات الأعمال ووحدات الإدارة"
  },
  "w-goal": {
    "es": "Las plantillas de objetivo de servicio son la meta de planificación",
    "hi": "सेवा लक्ष्य टेम्पलेट योजना का लक्ष्य हैं",
    "te": "సేవా లక్ష్య మూసలు ప్రణాళిక లక్ష్యం",
    "fr": "Les modèles d’objectif de service sont la cible du plan",
    "de": "Servicezielvorlagen sind das Planungsziel",
    "ja": "サービス目標テンプレートが計画の的",
    "ar": "قوالب هدف الخدمة هي هدف التخطيط"
  },
  "w-sched": {
    "es": "Los horarios son el plan que trabajan los agentes",
    "hi": "शेड्यूल वह योजना है जिस पर एजेंट काम करते हैं",
    "te": "షెడ్యూల్స్ ఏజెంట్లు పని చేసే ప్రణాళిక",
    "fr": "Les plannings sont le plan que suivent les agents",
    "de": "Pläne sind das, wonach Agenten arbeiten",
    "ja": "スケジュールは担当者が働く計画",
    "ar": "الجداول هي الخطة التي يعمل بها الوكلاء"
  },
  "w-intra": {
    "es": "El intradía y la adherencia comparan el plan con la sala",
    "hi": "इंट्राडे और अनुपालन योजना को फ़्लोर से मिलाते हैं",
    "te": "ఇంట్రాడే మరియు అనుసరణ ప్రణాళికను అంతస్తుతో పోలుస్తాయి",
    "fr": "L’intrajournée et l’adhérence comparent le plan à la salle",
    "de": "Intraday und Adherence vergleichen Plan und Fläche",
    "ja": "日中と順守は計画と現場を比べる",
    "ar": "خلال اليوم والالتزام يقارنان الخطة بالأرضية"
  },
  "w-off": {
    "es": "El tiempo libre es un cambio de horario con una regla",
    "hi": "टाइम ऑफ़ एक नियम के साथ शेड्यूल बदलाव है",
    "te": "టైమ్ ఆఫ్ నియమంతో కూడిన షెడ్యూల్ మార్పు",
    "fr": "Le congé est un changement de planning avec une règle",
    "de": "Freizeit ist eine Planänderung mit einer Regel",
    "ja": "休暇はルール付きの予定変更",
    "ar": "الإجازة تغيير جدول بقاعدة"
  },
  "w-cert": {
    "es": "La certificación de workforce es un examen con nombre",
    "hi": "कार्यबल प्रमाणन एक नामित परीक्षा है",
    "te": "వర్క్‌ఫోర్స్ ధృవీకరణ పేరున్న పరీక్ష",
    "fr": "La certification workforce est un examen nommé",
    "de": "Die Workforce-Zertifizierung ist eine benannte Prüfung",
    "ja": "ワークフォース認定は名前のある試験",
    "ar": "شهادة القوى العاملة امتحان باسم"
  },
  "w-forecast": {
    "es": "Un pronóstico tiene una vista corta y una vista larga",
    "hi": "पूर्वानुमान का एक छोटा दृश्य और एक लंबा दृश्य होता है",
    "te": "అంచనాకు చిన్న దృశ్యం మరియు పొడవైన దృశ్యం ఉంటాయి",
    "fr": "Une prévision a une vue courte et une vue longue",
    "de": "Eine Prognose hat eine kurze und eine lange Sicht",
    "ja": "予測には短い視点と長い視点がある",
    "ar": "للتوقع نظرة قصيرة ونظرة طويلة"
  },
  "w-generate": {
    "es": "Genera un horario desde un pronóstico que lo cubra",
    "hi": "ऐसे पूर्वानुमान से एक शेड्यूल बनाएँ जो उसे ढके",
    "te": "దాన్ని కవర్ చేసే అంచనా నుండి ఒక షెడ్యూల్ రూపొందించండి",
    "fr": "Générez un planning depuis une prévision qui le couvre",
    "de": "Einen Plan aus einer Prognose erzeugen, die ihn abdeckt",
    "ja": "それを覆う予測からスケジュールを一つ作る",
    "ar": "أنشئ جدولاً واحداً من توقع يغطيه"
  },
  "qm": {
    "es": "Calidad y grabación",
    "hi": "गुणवत्ता और रिकॉर्डिंग",
    "te": "నాణ్యత మరియు రికార్డింగ్",
    "fr": "Qualité et enregistrement",
    "de": "Qualität und Aufzeichnung",
    "ja": "品質と録音",
    "ar": "الجودة والتسجيل"
  },
  "m-overview": {
    "es": "La gestión de calidad evalúa la conversación",
    "hi": "गुणवत्ता प्रबंधन बातचीत का मूल्यांकन करता है",
    "te": "నాణ్యత నిర్వహణ సంభాషణను అంచనా వేస్తుంది",
    "fr": "La gestion de la qualité évalue la conversation",
    "de": "Qualitätsmanagement bewertet das Gespräch",
    "ja": "品質管理は会話を評価する",
    "ar": "إدارة الجودة تقيّم المحادثة"
  },
  "m-form": {
    "es": "Los formularios tienen preguntas y pesos",
    "hi": "फ़ॉर्म में प्रश्न और भार होते हैं",
    "te": "ఫారమ్‌లకు ప్రశ్నలు మరియు బరువులు ఉంటాయి",
    "fr": "Les formulaires ont des questions et des poids",
    "de": "Formulare haben Fragen und Gewichte",
    "ja": "フォームには質問と重みがある",
    "ar": "للنماذج أسئلة وأوزان"
  },
  "m-policy": {
    "es": "Las políticas de grabación eligen llamadas y retención",
    "hi": "रिकॉर्डिंग नीतियाँ कॉल और प्रतिधारण चुनती हैं",
    "te": "రికార్డింగ్ విధానాలు కాల్‌లను మరియు నిలుపుదలను ఎంచుకుంటాయి",
    "fr": "Les politiques d’enregistrement choisissent les appels et la rétention",
    "de": "Aufzeichnungsrichtlinien wählen Anrufe und Aufbewahrung",
    "ja": "録音ポリシーは通話と保存を選ぶ",
    "ar": "سياسات التسجيل تختار المكالمات والاحتفاظ"
  },
  "m-coach": {
    "es": "La tutoría y las disputas cierran el ciclo",
    "hi": "कोचिंग और विवाद चक्र बंद करते हैं",
    "te": "కోచింగ్ మరియు వివాదాలు చక్రాన్ని మూస్తాయి",
    "fr": "Coaching et contestations ferment la boucle",
    "de": "Coaching und Einsprüche schließen den Kreis",
    "ja": "コーチングと異議が輪を閉じる",
    "ar": "التدريب والاعتراضات يغلقان الحلقة"
  },
  "m-ai": {
    "es": "La puntuación de IA necesita STA, QM y tokens",
    "hi": "एआई स्कोरिंग को STA, QM और टोकन चाहिए",
    "te": "ఏఐ స్కోరింగ్‌కు STA, QM మరియు టోకెన్లు కావాలి",
    "fr": "Le score IA exige STA, QM et des jetons",
    "de": "KI-Bewertung braucht STA, QM und Tokens",
    "ja": "AI スコアには STA、QM、トークンが要る",
    "ar": "تسجيل الذكاء يحتاج STA وQM ورموزاً"
  },
  "m-export": {
    "es": "Retención, exportación y el motivo de la grabación",
    "hi": "प्रतिधारण, निर्यात और रिकॉर्ड करने का कारण",
    "te": "నిలుపుదల, ఎగుమతి మరియు రికార్డ్ చేసిన కారణం",
    "fr": "Rétention, export et la raison de l’enregistrement",
    "de": "Aufbewahrung, Export und der Grund der Aufnahme",
    "ja": "保存、書き出し、録音した理由",
    "ar": "الاحتفاظ والتصدير وسبب التسجيل"
  },
  "sta": {
    "es": "Analítica de voz y texto",
    "hi": "वाक् और पाठ विश्लेषण",
    "te": "స్పీచ్ మరియు టెక్స్ట్ విశ్లేషణ",
    "fr": "Analyse parole et texte",
    "de": "Sprach- und Textanalyse",
    "ja": "音声とテキストの分析",
    "ar": "تحليل الكلام والنص"
  },
  "s-scope": {
    "es": "STA lee la conversación después de que el canal la tiene",
    "hi": "चैनल के पास होने के बाद STA बातचीत पढ़ता है",
    "te": "ఛానెల్‌కు వచ్చిన తర్వాత STA సంభాషణను చదువుతుంది",
    "fr": "STA lit la conversation une fois que le canal l’a",
    "de": "STA liest das Gespräch, nachdem der Kanal es hat",
    "ja": "STA はチャネルが持った後に会話を読む",
    "ar": "يقرأ STA المحادثة بعد أن يحوزها القناة"
  },
  "s-sentiment": {
    "es": "El sentimiento es una etiqueta del texto, no un humor discutible",
    "hi": "भाव एक पाठ लेबल है, बहस करने लायक मूड नहीं",
    "te": "భావం వచనంపై లేబుల్, వాదించే మూడ్ కాదు",
    "fr": "Le sentiment est une étiquette du texte, pas une humeur à débattre",
    "de": "Stimmung ist ein Etikett am Text, keine streitbare Laune",
    "ja": "感情は本文のラベルであり、争う気分ではない",
    "ar": "المشاعر وسم على النص وليست مزاجاً يُجادَل"
  },
  "s-topics": {
    "es": "Temas, programas y frases son el diccionario",
    "hi": "विषय, प्रोग्राम और वाक्यांश शब्दकोश हैं",
    "te": "అంశాలు, ప్రోగ్రామ్‌లు మరియు పదబంధాలు నిఘంటువు",
    "fr": "Sujets, programmes et phrases sont le dictionnaire",
    "de": "Themen, Programme und Phrasen sind das Wörterbuch",
    "ja": "トピック、プログラム、語句が辞書",
    "ar": "المواضيع والبرامج والعبارات هي القاموس"
  },
  "s-empathy": {
    "es": "La empatía del agente es una conducta detectada y sigue siendo una pregunta del formulario",
    "hi": "एजेंट सहानुभूति एक पकड़ी गई व्यवहार है, फिर भी फ़ॉर्म प्रश्न",
    "te": "ఏజెంట్ సానుభూతి గుర్తించిన ప్రవర్తన, ఇంకా ఫారమ్ ప్రశ్న",
    "fr": "L’empathie de l’agent est un comportement détecté, encore une question de formulaire",
    "de": "Agentenempathie ist erkanntes Verhalten und bleibt eine Formularfrage",
    "ja": "担当者の共感は検出された振る舞いであり、依然フォームの質問",
    "ar": "تعاطف الوكيل سلوك مكتشف وما زال سؤال نموذج"
  },
  "s-search": {
    "es": "La búsqueda de contenido es cómo pruebas el diccionario",
    "hi": "कंटेंट खोज से आप शब्दकोश जाँचते हैं",
    "te": "కంటెంట్ శోధనతో నిఘంటువును పరీక్షిస్తారు",
    "fr": "La recherche de contenu teste le dictionnaire",
    "de": "Inhaltssuche prüft das Wörterbuch",
    "ja": "コンテンツ検索で辞書を試す",
    "ar": "بحث المحتوى هو كيف تختبر القاموس"
  },
  "s-timing": {
    "es": "El análisis completo y una transcripción más rápida son relojes distintos",
    "hi": "पूर्ण विश्लेषण और तेज़ प्रतिलेख अलग घड़ियाँ हैं",
    "te": "పూర్తి విశ్లేషణ మరియు వేగవంతమైన లిప్యంతరం వేర్వేరు గడియారాలు",
    "fr": "L’analyse complète et une transcription plus rapide sont deux horloges",
    "de": "Vollanalyse und schnellere Transkription sind verschiedene Uhren",
    "ja": "完全分析と速い文字起こしは別の時計",
    "ar": "التحليل الكامل والنص الأسرع ساعتان مختلفتان"
  },
  "ai": {
    "es": "Genesys AI y bots",
    "hi": "Genesys AI और बॉट",
    "te": "Genesys AI మరియు బాట్‌లు",
    "fr": "Genesys AI et bots",
    "de": "Genesys AI und Bots",
    "ja": "Genesys AI とボット",
    "ar": "Genesys AI والروبوتات"
  },
  "g-kinds": {
    "es": "Dos tipos de bot en Architect, y Copilot junto al agente",
    "hi": "Architect में दो बॉट प्रकार, और एजेंट के पास Copilot",
    "te": "Architectలో రెండు బాట్ రకాలు, ఏజెంట్ పక్కన Copilot",
    "fr": "Deux types de bots Architect, plus Copilot près de l’agent",
    "de": "Zwei Architect-Bot-Typen, plus Copilot neben dem Agenten",
    "ja": "Architect のボットは二種、Copilot は担当者の横",
    "ar": "نوعا روبوت في Architect، وCopilot بجانب الوكيل"
  },
  "g-dialog": {
    "es": "Los flujos de Dialog Engine son intenciones de voz y digitales",
    "hi": "डायलॉग इंजन बॉट फ़्लो आवाज़ और डिजिटल इंटेंट हैं",
    "te": "డైలాగ్ ఇంజిన్ బాట్ ఫ్లోలు వాయిస్ మరియు డిజిటల్ ఉద్దేశాలు",
    "fr": "Les flux Dialog Engine sont des intentions voix et numériques",
    "de": "Dialog-Engine-Flows sind Sprach- und Digital-Intents",
    "ja": "Dialog Engine のフローは音声とデジタルのインテント",
    "ar": "تدفقات Dialog Engine نوايا صوتية ورقمية"
  },
  "g-digital": {
    "es": "Los flujos de bot digital son otra llamada",
    "hi": "डिजिटल बॉट फ़्लो एक अलग कॉल हैं",
    "te": "డిజిటల్ బాట్ ఫ్లోలు వేరే పిలుపు",
    "fr": "Les flux de bot numérique sont un autre appel",
    "de": "Digitale Bot-Flows sind ein anderer Aufruf",
    "ja": "デジタルボットのフローは別の呼び出し",
    "ar": "تدفقات الروبوت الرقمي نداء مختلف"
  },
  "g-fail": {
    "es": "Todo bot tiene una salida de fallo hacia una cola",
    "hi": "हर बॉट का एक विफलता निकास क्यू की ओर है",
    "te": "ప్రతి బాట్‌కు క్యూ వైపు వైఫల్య నిష్క్రమణ ఉంటుంది",
    "fr": "Chaque bot a une sortie d’échec vers une file",
    "de": "Jeder Bot hat einen Fehlerausgang zu einer Queue",
    "ja": "どのボットにもキューへの失敗出口がある",
    "ar": "لكل روبوت مخرج فشل نحو قائمة انتظار"
  },
  "g-copilot": {
    "es": "Agent Copilot ayuda a quien se quedó en la interacción",
    "hi": "एजेंट Copilot उस व्यक्ति की मदद करता है जो बातचीत पर रहा",
    "te": "ఏజెంట్ Copilot పరస్పర చర్యపై ఉన్న వ్యక్తికి సహాయపడుతుంది",
    "fr": "Agent Copilot aide la personne restée sur l’interaction",
    "de": "Agent Copilot hilft der Person, die in der Interaktion blieb",
    "ja": "Agent Copilot は対話に残った人を助ける",
    "ar": "يساعد Agent Copilot من بقي في التفاعل"
  },
  "g-tokens": {
    "es": "Los tokens son una asignación publicada y una proporción de FAQ que vuelves a leer",
    "hi": "टोकन एक प्रकाशित आवंटन हैं और एक FAQ अनुपात जिसे फिर पढ़ें",
    "te": "టోకెన్లు ప్రచురిత కేటాయింపు మరియు మళ్లీ చదివే FAQ నిష్పత్తి",
    "fr": "Les jetons sont une dotation publiée et un ratio FAQ à relire",
    "de": "Tokens sind eine veröffentlichte Zuteilung und ein FAQ-Verhältnis zum Nachlesen",
    "ja": "トークンは公開された割当と、読み返す FAQ 比率",
    "ar": "الرموز حصة منشورة ونسبة أسئلة شائعة تعيد قراءتها"
  },
  "g-cert": {
    "es": "Los exámenes de IA están nombrados en el catálogo, uno cada uno",
    "hi": "एआई परीक्षाएँ कैटलॉग पर नाम से हैं, प्रत्येक एक",
    "te": "ఏఐ పరీక్షలు కేటలాగ్‌లో పేరుతో ఉన్నాయి, ఒక్కొక్కటి",
    "fr": "Les examens IA sont nommés au catalogue, un chacun",
    "de": "Die KI-Prüfungen stehen namentlich im Katalog, je eine",
    "ja": "AI 試験はカタログに名前があり、それぞれ一つ",
    "ar": "امتحانات الذكاء مسمّاة في الكتالوج، واحد لكل منها"
  },
  "api": {
    "es": "API de la plataforma",
    "hi": "प्लेटफ़ॉर्म API",
    "te": "ప్లాట్‌ఫారమ్ APIలు",
    "fr": "API de la plateforme",
    "de": "Plattform-APIs",
    "ja": "プラットフォーム API",
    "ar": "واجهات المنصة"
  },
  "p-center": {
    "es": "El Developer Center es el mapa. Este laboratorio no es un cliente.",
    "hi": "डेवलपर सेंटर नक्शा है। यह लैब क्लाइंट नहीं है।",
    "te": "డెవలపర్ సెంటర్ పటం. ఈ ల్యాబ్ క్లయింట్ కాదు.",
    "fr": "Le Developer Center est la carte. Ce labo n’est pas un client.",
    "de": "Das Developer Center ist die Karte. Dieses Lab ist kein Client.",
    "ja": "Developer Center が地図。このラボはクライアントではない。",
    "ar": "مركز المطوّرين هو الخريطة. هذا المختبر ليس عميلاً."
  },
  "p-grants": {
    "es": "Elige la concesión que coincida con quién ejecuta la llamada",
    "hi": "वह ग्रांट चुनें जो कॉल चलाने वाले से मेल खाए",
    "te": "కాల్ ఎవరిగా నడుస్తుందో దానికి సరిపోయే గ్రాంట్ ఎంచుకోండి",
    "fr": "Choisissez l’octroi selon qui exécute l’appel",
    "de": "Wähle den Grant, der dazu passt, als wer der Aufruf läuft",
    "ja": "呼び出しが誰として動くかに合うグラントを選ぶ",
    "ar": "اختر المنحة التي تطابق من يعمل النداء باسمه"
  },
  "p-cc": {
    "es": "Las credenciales de cliente no tienen usuario, así que users/me es la llamada equivocada",
    "hi": "क्लाइंट क्रेडेंशियल का कोई उपयोगकर्ता नहीं, इसलिए users/me गलत कॉल है",
    "te": "క్లయింట్ క్రెడెన్షియల్స్‌కు వినియోగదారు లేడు, కాబట్టి users/me తప్పు పిలుపు",
    "fr": "Les identifiants client n’ont pas d’utilisateur, donc users/me est le mauvais appel",
    "de": "Client Credentials haben keinen Benutzer, also ist users/me der falsche Aufruf",
    "ja": "クライアント資格情報にユーザーはいない。users/me は誤った呼び出し",
    "ar": "بيانات اعتماد العميل بلا مستخدم، لذا users/me النداء الخطأ"
  },
  "p-implicit": {
    "es": "La concesión implícita es una migración, no un diseño nuevo",
    "hi": "इम्प्लिसिट ग्रांट एक माइग्रेशन है, नया डिज़ाइन नहीं",
    "te": "ఇంప్లిసిట్ గ్రాంట్ ఒక మైగ్రేషన్, కొత్త రూపకల్పన కాదు",
    "fr": "L’octroi implicite est une migration, pas un nouveau dessin",
    "de": "Implicit Grant ist eine Migration, kein neues Design",
    "ja": "インプリシットグラントは移行であり、新しい設計ではない",
    "ar": "المنحة الضمنية ترحيل وليست تصميماً جديداً"
  },
  "p-hosts": {
    "es": "El host de acceso y el host de API son un par que se consulta",
    "hi": "लॉगिन होस्ट और API होस्ट एक जोड़ी है जिसे देखना है",
    "te": "లాగిన్ హోస్ట్ మరియు API హోస్ట్ చూడాల్సిన జంట",
    "fr": "L’hôte de connexion et l’hôte d’API sont une paire à vérifier",
    "de": "Login-Host und API-Host sind ein Paar zum Nachschlagen",
    "ja": "ログインホストと API ホストは調べる組",
    "ar": "مضيف الدخول ومضيف الواجهة زوج تبحث عنه"
  },
  "p-roles": {
    "es": "Los pares de rol y división son el permiso real",
    "hi": "भूमिका और डिवीजन की जोड़ी असली अनुमति है",
    "te": "పాత్ర మరియు డివిజన్ జంటే నిజమైన అనుమతి",
    "fr": "Les paires rôle et division sont la vraie permission",
    "de": "Rollen- und Divisionspaare sind die echte Berechtigung",
    "ja": "ロールとディビジョンの組が本当の権限",
    "ar": "أزواج الدور والقسم هي الإذن الحقيقي"
  },
  "p-scim": {
    "es": "SCIM y otra sincronización de directorio empiezan igual con un cliente OAuth",
    "hi": "SCIM और अन्य निर्देशिका सिंक भी एक OAuth क्लाइंट से शुरू होते हैं",
    "te": "SCIM మరియు ఇతర డైరెక్టరీ సింక్ కూడా OAuth క్లయింట్‌తో మొదలవుతాయి",
    "fr": "SCIM et les autres synchros d’annuaire commencent par un client OAuth",
    "de": "SCIM und andere Verzeichnissyncs beginnen mit einem OAuth-Client",
    "ja": "SCIM も他のディレクトリ同期も OAuth クライアントから始まる",
    "ar": "SCIM ومزامنة الدليل الأخرى تبدآن بعميل OAuth"
  },
  "crm": {
    "es": "AppFoundry y CRM",
    "hi": "AppFoundry और CRM",
    "te": "AppFoundry మరియు CRM",
    "fr": "AppFoundry et CRM",
    "de": "AppFoundry und CRM",
    "ja": "AppFoundry と CRM",
    "ar": "AppFoundry وإدارة العملاء"
  },
  "i-market": {
    "es": "AppFoundry es el mercado, no una función que supongas instalada",
    "hi": "AppFoundry बाज़ार है, मानकर स्थापित सुविधा नहीं",
    "te": "AppFoundry మార్కెట్, ఇన్‌స్టాల్ అయిందని అనుకునే ఫీచర్ కాదు",
    "fr": "AppFoundry est la place de marché, pas une fonction supposée installée",
    "de": "AppFoundry ist der Marktplatz, keine Funktion, die man als installiert annimmt",
    "ja": "AppFoundry は市場であり、入っていると思い込む機能ではない",
    "ar": "AppFoundry سوق وليس ميزة تفترض أنها مثبّتة"
  },
  "i-sf": {
    "es": "Genesys Cloud para Salesforce es una incrustación documentada",
    "hi": "Salesforce के लिए Genesys Cloud एक दस्तावेज़ी एम्बेड है",
    "te": "Salesforce కోసం Genesys Cloud డాక్యుమెంట్ చేసిన ఎంబెడ్",
    "fr": "Genesys Cloud pour Salesforce est une intégration documentée",
    "de": "Genesys Cloud für Salesforce ist eine dokumentierte Einbettung",
    "ja": "Salesforce 向け Genesys Cloud は文書化された埋め込み",
    "ar": "Genesys Cloud لـ Salesforce تضمين موثّق"
  },
  "i-sf-oauth": {
    "es": "Las acciones de datos de Salesforce pasan a credenciales de cliente OAuth",
    "hi": "Salesforce डेटा क्रियाएँ OAuth क्लाइंट क्रेडेंशियल पर जाती हैं",
    "te": "Salesforce డేటా చర్యలు OAuth క్లయింట్ క్రెడెన్షియల్స్‌కు వెళ్తాయి",
    "fr": "Les actions de données Salesforce passent aux identifiants client OAuth",
    "de": "Salesforce-Datenaktionen wechseln zu OAuth-Client-Credentials",
    "ja": "Salesforce のデータアクションは OAuth クライアント資格情報へ移る",
    "ar": "إجراءات بيانات Salesforce تنتقل إلى بيانات اعتماد عميل OAuth"
  },
  "i-zd": {
    "es": "Zendesk tiene su propia página, con una idea de incrustación parecida",
    "hi": "Zendesk का अपना पृष्ठ है, समान एम्बेड विचार के साथ",
    "te": "Zendeskకు సొంత పేజీ ఉంది, ఇలాంటి ఎంబెడ్ ఆలోచనతో",
    "fr": "Zendesk a sa propre page, avec une idée d’intégration proche",
    "de": "Zendesk hat eine eigene Seite, mit einer ähnlichen Einbettung",
    "ja": "Zendesk には似た埋め込みの独自ページがある",
    "ar": "لـ Zendesk صفحته، بفكرة تضمين مشابهة"
  },
  "i-other": {
    "es": "Dynamics, ServiceNow y el resto se quedan en el mercado",
    "hi": "Dynamics, ServiceNow और बाकी बाज़ार पर रहते हैं",
    "te": "Dynamics, ServiceNow మరియు మిగతావి మార్కెట్‌లోనే ఉంటాయి",
    "fr": "Dynamics, ServiceNow et le reste restent sur la place de marché",
    "de": "Dynamics, ServiceNow und der Rest bleiben im Marktplatz",
    "ja": "Dynamics、ServiceNow、その他は市場に残る",
    "ar": "Dynamics وServiceNow والبقية تبقى في السوق"
  },
  "i-fail": {
    "es": "Un fallo de CRM no es un fallo de ACD",
    "hi": "CRM की विफलता ACD की विफलता नहीं है",
    "te": "CRM వైఫల్యం ACD వైఫల్యం కాదు",
    "fr": "Une panne CRM n’est pas une panne ACD",
    "de": "Ein CRM-Fehler ist kein ACD-Fehler",
    "ja": "CRM の失敗は ACD の失敗ではない",
    "ar": "فشل CRM ليس فشل ACD"
  },
  "migration": {
    "es": "Migración",
    "hi": "माइग्रेशन",
    "te": "మైగ్రేషన్",
    "fr": "Migration",
    "de": "Migration",
    "ja": "移行",
    "ar": "الترحيل"
  },
  "x-rebuild": {
    "es": "Nada importa tu enrutamiento antiguo por arte de magia",
    "hi": "कुछ भी आपके पुराने रूटिंग को जादू से नहीं लाता",
    "te": "మీ పాత రూటింగ్‌ను మాయాజాలంతో ఏదీ దిగుమతి చేయదు",
    "fr": "Rien n’importe votre ancien routage par magie",
    "de": "Nichts importiert das alte Routing von allein",
    "ja": "古いルーティングは魔法では入らない",
    "ar": "لا شيء يستورد توجيهك القديم بالسحر"
  },
  "x-engage": {
    "es": "Engage y PureConnect se vuelven flujos y colas",
    "hi": "Engage और PureConnect फ़्लो और क्यू बनते हैं",
    "te": "Engage మరియు PureConnect ఫ్లోలు మరియు క్యూలు అవుతాయి",
    "fr": "Engage et PureConnect deviennent des flux et des files",
    "de": "Engage und PureConnect werden Flows und Queues",
    "ja": "Engage と PureConnect はフローとキューになる",
    "ar": "Engage وPureConnect يصبحان تدفقات وقوائم"
  },
  "x-ivr": {
    "es": "El IVR se vuelve tareas, menús y audio de Architect",
    "hi": "IVR Architect के कार्य, मेनू और ऑडियो बनता है",
    "te": "IVR Architect టాస్క్‌లు, మెనూలు మరియు ఆడియో అవుతుంది",
    "fr": "L’IVR devient tâches, menus et audio Architect",
    "de": "IVR wird zu Architect-Aufgaben, Menüs und Audio",
    "ja": "IVR は Architect のタスク、メニュー、音声になる",
    "ar": "يصبح IVR مهام Architect وقوائم وصوتاً"
  },
  "x-ucce": {
    "es": "Los grupos de habilidad y las colas de precisión de UCCE no son colas de Genesys",
    "hi": "UCCE स्किल ग्रुप और प्रिसिजन क्यू Genesys क्यू नहीं हैं",
    "te": "UCCE స్కిల్ గ్రూపులు మరియు ప్రెసిషన్ క్యూలు Genesys క్యూలు కావు",
    "fr": "Les groupes de compétences et files de précision UCCE ne sont pas des files Genesys",
    "de": "UCCE-Skillgruppen und Precision Queues sind keine Genesys-Queues",
    "ja": "UCCE のスキルグループとプレシジョンキューは Genesys のキューではない",
    "ar": "مجموعات مهارة UCCE وطوابير الدقة ليست قوائم Genesys"
  },
  "x-uccx": {
    "es": "UCCX es un centro más pequeño con la misma regla de reconstrucción",
    "hi": "UCCX एक छोटा केंद्र है, पुनर्निर्माण का नियम वही है",
    "te": "UCCX చిన్న కేంద్రం, పునర్నిర్మాణ నియమం అదే",
    "fr": "UCCX est un centre plus petit avec la même règle de reconstruction",
    "de": "UCCX ist ein kleineres Center mit derselben Neuaufbauregel",
    "ja": "UCCX は小さいセンターで、作り直しの規則は同じ",
    "ar": "UCCX مركز أصغر وقاعدة إعادة البناء نفسها"
  },
  "x-cucm": {
    "es": "CUCM se queda. BYOC es la puerta, no un clúster de reemplazo.",
    "hi": "CUCM रहता है। BYOC द्वार है, बदलने वाला क्लस्टर नहीं।",
    "te": "CUCM ఉంటుంది. BYOC తలుపు, భర్తీ క్లస్టర్ కాదు.",
    "fr": "CUCM reste. BYOC est la porte, pas un cluster de remplacement.",
    "de": "CUCM bleibt. BYOC ist die Tür, kein Ersatz-Cluster.",
    "ja": "CUCM は残る。BYOC は扉であり、置き換えクラスタではない。",
    "ar": "CUCM يبقى. BYOC هو الباب وليس عنقوداً بديلاً."
  },
  "x-webex": {
    "es": "Webex es un vecino, no una página que este laboratorio finja resumir",
    "hi": "Webex एक पड़ोसी है, यह लैब उसका सार नहीं गढ़ती",
    "te": "Webex పొరుగు, ఈ ల్యాబ్ దాన్ని సంగ్రహిస్తున్నట్లు నటించదు",
    "fr": "Webex est un voisin, pas une page que ce labo prétend résumer",
    "de": "Webex ist ein Nachbar, keine Seite, die dieses Lab zusammenfasst",
    "ja": "Webex は隣人であり、このラボが要約するページではない",
    "ar": "Webex جار وليس صفحة يدّعي هذا المختبر تلخيصها"
  },
  "x-cut": {
    "es": "Corta un número, luego la cola, luego las personas",
    "hi": "एक नंबर काटें, फिर क्यू, फिर लोग",
    "te": "ఒక నంబర్ కట్ చేయండి, తర్వాత క్యూ, తర్వాత వ్యక్తులు",
    "fr": "Basculez un numéro, puis la file, puis les personnes",
    "de": "Eine Nummer umstellen, dann die Queue, dann die Menschen",
    "ja": "番号を一つ切り替え、次にキュー、次に人",
    "ar": "حوّل رقماً واحداً ثم القائمة ثم الأشخاص"
  },
  "ecosystem": {
    "es": "Ecosistema",
    "hi": "पारिस्थितिकी",
    "te": "పర్యావరణం",
    "fr": "Écosystème",
    "de": "Ökosystem",
    "ja": "エコシステム",
    "ar": "المنظومة"
  },
  "z-map": {
    "es": "La conversación cruza una lista corta de sistemas",
    "hi": "बातचीत प्रणालियों की एक छोटी सूची पार करती है",
    "te": "సంభాషణ కొద్ది వ్యవస్థల జాబితాను దాటుతుంది",
    "fr": "La conversation traverse une courte liste de systèmes",
    "de": "Das Gespräch kreuzt eine kurze Liste von Systemen",
    "ja": "会話は短いシステムの列を渡る",
    "ar": "تعبر المحادثة قائمة قصيرة من الأنظمة"
  },
  "z-sisters": {
    "es": "WFM, QM, E911, analítica, CRM y bots son hermanas",
    "hi": "WFM, QM, E911, विश्लेषण, CRM और बॉट बहनें हैं",
    "te": "WFM, QM, E911, విశ్లేషణ, CRM మరియు బాట్‌లు సోదరులు",
    "fr": "WFM, QM, E911, analytique, CRM et bots sont sœurs",
    "de": "WFM, QM, E911, Analytik, CRM und Bots sind Schwestern",
    "ja": "WFM、QM、E911、分析、CRM、ボットは姉妹",
    "ar": "WFM وQM وE911 والتحليل وCRM والروبوتات شقيقات"
  },
  "z-bridge": {
    "es": "El puente con Cisco es una traducción, con ambas citas a la vista",
    "hi": "Cisco पुल एक अनुवाद है, दोनों उद्धरण दिखते हैं",
    "te": "సిస్కో వంతెన ఒక అనువాదం, రెండు ఉల్లేఖనాలు కనిపిస్తాయి",
    "fr": "Le pont Cisco est une traduction, avec les deux citations",
    "de": "Die Cisco-Brücke ist eine Übersetzung, beide Quellen sichtbar",
    "ja": "Cisco の橋は翻訳で、両方の出典が見える",
    "ar": "جسر سيسكو ترجمة والمصدران ظاهران"
  },
  "z-certs": {
    "es": "Lee el catálogo por nombre y luego el anuncio",
    "hi": "कैटलॉग नाम से पढ़ें, फिर घोषणा",
    "te": "కేటలాగ్‌ను పేరుతో చదవండి, తర్వాత ప్రకటన",
    "fr": "Lisez le catalogue par nom, puis l’annonce",
    "de": "Den Katalog nach Namen lesen, dann die Ankündigung",
    "ja": "カタログを名前で読み、次に告知",
    "ar": "اقرأ الكتالوج بالاسم ثم الإعلان"
  },
  "z-interview": {
    "es": "Las respuestas de entrevista citan una página, no una vibra",
    "hi": "साक्षात्कार उत्तर एक पृष्ठ उद्धृत करते हैं, मूड नहीं",
    "te": "ఇంటర్వ్యూ సమాధానాలు పేజీని ఉల్లేఖిస్తాయి, అనుభూతిని కాదు",
    "fr": "Les réponses d’entretien citent une page, pas une ambiance",
    "de": "Interviewantworten zitieren eine Seite, keine Stimmung",
    "ja": "面接の答えは雰囲気ではなくページを引く",
    "ar": "إجابات المقابلة تستشهد بصفحة لا بانطباع"
  },
  "z-refuse": {
    "es": "Lo que este laboratorio no inventará",
    "hi": "यह लैब क्या नहीं गढ़ेगी",
    "te": "ఈ ల్యాబ్ ఏమి కల్పించదు",
    "fr": "Ce que ce laboratoire n’inventera pas",
    "de": "Was dieses Lab nicht erfinden wird",
    "ja": "このラボが創作しないこと",
    "ar": "ما لن يخترعه هذا المختبر"
  },
  "predictive": {
    "es": "Predictive Engagement",
    "hi": "Predictive Engagement",
    "te": "Predictive Engagement",
    "fr": "Predictive Engagement",
    "de": "Predictive Engagement",
    "ja": "Predictive Engagement",
    "ar": "Predictive Engagement"
  },
  "pe-what": {
    "es": "Predictive Engagement observa el sitio, no la matemática de la cola",
    "hi": "Predictive Engagement साइट देखता है, क्यू का गणित नहीं",
    "te": "Predictive Engagement సైట్‌ను చూస్తుంది, క్యూ గణితాన్ని కాదు",
    "fr": "Predictive Engagement regarde le site, pas le calcul de la file",
    "de": "Predictive Engagement beobachtet die Site, nicht die Queue-Mathematik",
    "ja": "Predictive Engagement はサイトを見て、キューの計算は見ない",
    "ar": "يراقب Predictive Engagement الموقع لا حساب قائمة الانتظار"
  },
  "pe-track": {
    "es": "Messenger sigue la mensajería web. El fragmento antiguo sigue el chat web.",
    "hi": "Messenger वेब मैसेजिंग ट्रैक करता है। पुराना स्निपेट वेब चैट ट्रैक करता है।",
    "te": "Messenger వెబ్ మెసేజింగ్‌ను ట్రాక్ చేస్తుంది. పాత స్నిప్పెట్ వెబ్ చాట్‌ను ట్రాక్ చేస్తుంది.",
    "fr": "Messenger suit la messagerie web. L’ancien extrait suit le chat web.",
    "de": "Messenger verfolgt Web Messaging. Das alte Snippet verfolgt Webchat.",
    "ja": "Messenger はウェブメッセージを追う。古いスニペットはウェブチャットを追う。",
    "ar": "يتتبع Messenger مراسلة الويب. المقتطف القديم يتتبع دردشة الويب."
  },
  "pe-segments": {
    "es": "Un segmento coincide con visitantes que cumplen cada condición listada",
    "hi": "सेगमेंट उन आगंतुकों से मेल खाता है जो हर सूचीबद्ध शर्त पूरी करते हैं",
    "te": "సెగ్మెంట్ జాబితా చేసిన ప్రతి షరతు పాటించే సందర్శకులకు సరిపోతుంది",
    "fr": "Un segment correspond aux visiteurs qui remplissent chaque condition listée",
    "de": "Ein Segment trifft Besucher, die jede gelistete Bedingung erfüllen",
    "ja": "セグメントは挙げた条件をすべて満たす訪問者に合う",
    "ar": "يطابق المقطع الزوار الذين يحققون كل شرط مذكور"
  },
  "pe-map": {
    "es": "Un mapa de acción se cualifica antes de ofrecerse",
    "hi": "एक्शन मैप पेश होने से पहले योग्य होता है",
    "te": "ఆఫర్ కాకముందే యాక్షన్ మ్యాప్ అర్హమవుతుంది",
    "fr": "Une carte d’action est qualifiée avant d’être offerte",
    "de": "Eine Action Map wird qualifiziert, bevor sie angeboten wird",
    "ja": "アクションマップは提示の前に適格になる",
    "ar": "تتأهل خريطة الإجراء قبل أن تُعرض"
  },
  "pe-outcomes": {
    "es": "Journey Outcomes tienen una fecha de fin publicada",
    "hi": "जर्नी आउटकम की प्रकाशित समाप्ति तिथि है",
    "te": "జర్నీ అవుట్‌కమ్‌లకు ప్రచురిత ముగింపు తేదీ ఉంది",
    "fr": "Les Journey Outcomes ont une date de fin publiée",
    "de": "Journey Outcomes haben ein veröffentlichtes Enddatum",
    "ja": "Journey Outcomes には公開された終了日がある",
    "ar": "لـ Journey Outcomes تاريخ انتهاء منشور"
  },
  "pe-flow": {
    "es": "Un flujo de Architect puede ser la acción y también lo que debes editar",
    "hi": "एक Architect फ़्लो क्रिया हो सकता है और वही जिसे संपादित करना है",
    "te": "ఒక Architect ఫ్లో చర్య కావచ్చు, మీరు సవరించాల్సినది కూడా",
    "fr": "Un flux Architect peut être l’action et aussi ce qu’il faut modifier",
    "de": "Ein Architect-Flow kann die Aktion sein und zugleich das, was du ändern musst",
    "ja": "Architect のフローはアクションであり、編集すべきものでもある",
    "ar": "قد يكون تدفق Architect هو الإجراء وأيضاً ما يجب تعديله"
  },
  "pe-report": {
    "es": "Demuestra el mapa con Live Now y los informes de rendimiento",
    "hi": "Live Now और प्रदर्शन रिपोर्ट से मैप साबित करें",
    "te": "Live Now మరియు పనితీరు నివేదికలతో మ్యాప్‌ను నిరూపించండి",
    "fr": "Prouvez la carte avec Live Now et les rapports de performance",
    "de": "Die Map mit Live Now und den Leistungsberichten belegen",
    "ja": "Live Now と性能レポートでマップを確かめる",
    "ar": "أثبت الخريطة عبر Live Now وتقارير الأداء"
  }
};

export function heading(id, lang, fallback) {
  if (!lang || lang === "en") return fallback || "";
  const row = HEADS[id];
  if (!row) return fallback || "";
  return row[lang] || fallback || "";
}
