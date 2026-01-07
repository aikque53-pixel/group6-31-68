#!/usr/bin/env python3
"""
Generate Thai translations for questions 101-132
"""

import json

questions_data = [
    {
        "num": 101,
        "q": "Which Byzantine emperor codified Roman law in the Corpus Juris Civilis?",
        "c": ["Justinian I", "Heraclius", "Constantine VII", "Basil II"],
        "q_th": "จักรพรรดิไบแซนไทน์องค์ใดได้รวบรวมกฎหมายโรมันในลัทธิ Corpus Juris Civilis",
        "c_th": ["จัสตินิยาน I", "เฮราคลิอุส", "คอนสแตนติน VII", "บาซิล II"]
    },
    {
        "num": 102,
        "q": "Which civilization is credited with constructing the city of Tikal?",
        "c": ["Maya", "Aztec", "Olmec", "Toltec"],
        "q_th": "อารยธรรมใดสร้างเมืองติกัล",
        "c_th": ["มายา", "แอซเทก", "โอลเมก", "โทลเทก"]
    },
    {
        "num": 103,
        "q": "Which Spanish city became the colonial capital of Peru after the conquest?",
        "c": ["Lima", "Cusco", "Quito", "Potosí"],
        "q_th": "เมืองสเปนใดกลายเป็นเมืองหลวงของอาณานิคมเปรู หลังการพิชิต",
        "c_th": ["ลิมา", "กุสโก", "กีโต", "โปโตซี"]
    },
    {
        "num": 104,
        "q": "Which World War II battle involved Allied operations to capture an island chain including Guadalcanal?",
        "c": ["Guadalcanal Campaign", "Midway", "Iwo Jima", "Leyte Gulf"],
        "q_th": "การรบในสงครามโลกครั้งที่สองใดเกี่ยวข้องกับการปฏิบัติการของพันธมิตรเพื่อครอบครองเกาะ รวมถึงกวัดัลคานัล",
        "c_th": ["แคมเปญกวัดัลคานัล", "มิดเวย์", "อิโว จิมา", "อ่าวเลย์เต"]
    },
    {
        "num": 105,
        "q": "Which West African kingdom was known for its ashanti golden stool and gold trade?",
        "c": ["Ashanti", "Mali", "Ghana", "Songhai"],
        "q_th": "อาณาจักรแอฟริกาตะวันตกใดเป็นที่รู้จักเพราะเก้าอี้ทองคำ Ashanti และการค้าขายทองคำ",
        "c_th": ["แอชแอนตี", "มาลี", "กานา", "สองไห"]
    },
    {
        "num": 106,
        "q": "Which Mauryan emperor famously converted to Buddhism and spread it across his realm?",
        "c": ["Ashoka", "Chandragupta", "Bindusara", "Harsha"],
        "q_th": "จักรพรรดิ Mauryan องค์ใดศรัทธาพุทธศาสนาและเผยแพร่ทั่วปกครอง",
        "c_th": ["อโศกะ", "จันทรคุปตะ", "บินทุสารา", "หรรษะ"]
    },
    {
        "num": 107,
        "q": "Which scientist published the laws of motion and universal gravitation in the 17th century?",
        "c": ["Isaac Newton", "Galileo Galilei", "Johannes Kepler", "Tycho Brahe"],
        "q_th": "นักวิทยาศาสตร์องค์ใดตีพิมพ์กฎการเคลื่อนที่และกฎความโน้มถ่วงสากลในศตวรรษที่ 17",
        "c_th": ["ไอแซก นิวตัน", "กาลิเลโอ กาลิเลอี", "โยฮันเนส เคปเลอร์", "ไทโค บราห์"]
    },
    {
        "num": 108,
        "q": "Which U.S. president led the country during the majority of World War II?",
        "c": ["Franklin D. Roosevelt", "Harry S. Truman", "Dwight D. Eisenhower", "Woodrow Wilson"],
        "q_th": "ประธานาธิบดีสหรัฐฯ องค์ใดนำประเทศในระหว่างสงครามโลกครั้งที่สอง",
        "c_th": ["แฟรงคลิน ดี. โรสเวลต์", "แฮร์รี่ เอส. ทรูแมน", "ดไวท์ ดี. ไอเซนหาวเวอร์", "วูดโรว์ วิลสัน"]
    },
    {
        "num": 109,
        "q": "Which ancient civilization in the Andes is known for the Nazca Lines?",
        "c": ["Nazca culture", "Moche", "Chavín", "Tiwanaku"],
        "q_th": "อารยธรรมโบราณในแอนดีส องค์ใดเป็นที่รู้จักเพราะเส้นนาซกา",
        "c_th": ["วัฒนธรรมนาซกา", "โมเช่", "ชาวิน", "ติวานากุ"]
    },
    {
        "num": 110,
        "q": "Which Victorian era policy affected non-European immigration to Australia in the early 20th century?",
        "c": ["White Australia Policy", "Immigration Restriction Act", "Citizenship Act", "Pacific Solution"],
        "q_th": "นโยบายสมัยวิกตอเรียใดส่งผลกระทบต่อการย้ายถิ่นของชาวต่างชาติที่ไม่ใช่ยุโรปไปออสเตรเลีย ในต้นศตวรรษที่ 20",
        "c_th": ["นโยบายออสเตรเลียสีขาว", "พระราชกฤษฎีกาจำกัดการย้ายถิ่น", "พระราชกฤษฎีกาสัญชาติ", "ปัญหาแปซิฟิก"]
    },
    {
        "num": 111,
        "q": "Which city was founded by Alexander the Great and later became a major center of Hellenistic culture in Egypt?",
        "c": ["Alexandria", "Carthage", "Memphis", "Thebes"],
        "q_th": "เมืองใดถูกก่อตั้งโดยเอเลกซานเดอร์มหาราช และต่อมากลายเป็นศูนย์กลางของวัฒนธรรมเฮลเลนิสติกในอียิปต์",
        "c_th": ["อเล็กซานเดรีย", "คาร์เธจ", "เมมฟิส", "เธบส์"]
    },
    {
        "num": 112,
        "q": "Which island nation east of China adopted Buddhism, Confucianism, and its own samurai culture?",
        "c": ["Japan", "Korea", "Philippines", "Taiwan"],
        "q_th": "ชาติเกาะใดทางตะวันออกของจีนรับเอาพุทธศาสนา คอนฟูเชียนิสม และวัฒนธรรมซามูไร",
        "c_th": ["ญี่ปุ่น", "เกาหลี", "ฟิลิปปินส์", "ไต้หวัน"]
    },
    {
        "num": 113,
        "q": "Which people from Scandinavia were known for raiding and trading across Europe from the 8th–11th centuries?",
        "c": ["Vikings", "Franks", "Saxons", "Angles"],
        "q_th": "ชนชาติใดจากสแกนดิเนเวียเป็นที่รู้จักในการลักทุน และการค้าขายทั่วยุโรป ตั้งแต่ศตวรรษที่ 8-11",
        "c_th": ["ไวกิ้ง", "แฟรงก์", "แซกสัน", "แองเกิล"]
    },
    {
        "num": 114,
        "q": "Which document, ratified in 1788, established the framework of the United States federal government?",
        "c": ["United States Constitution", "Articles of Confederation", "Declaration of Independence", "Bill of Rights"],
        "q_th": "เอกสารใดที่ได้รับการ批准ในปี 1788 สร้างกรอบการปกครองกลางสหรัฐฯ",
        "c_th": ["รัฐธรรมนูญสหรัฐฯ", "บทความแห่งสหพันธ์", "ปฏิญญาอิสรภาพ", "บิลแห่งสิทธิ"]
    },
    {
        "num": 115,
        "q": "Which European language is the primary language of Brazil?",
        "c": ["Portuguese", "Spanish", "French", "English"],
        "q_th": "ภาษายุโรปใดเป็นภาษาหลักของบราซิล",
        "c_th": ["โปรตุเกส", "สเปน", "ฝรั่งเศส", "อังกฤษ"]
    },
    {
        "num": 116,
        "q": "Which indigenous people are the tangata whenua (people of the land) of New Zealand?",
        "c": ["Māori", "Samoans", "Fijians", "Tongan"],
        "q_th": "ชนพื้นเมืองใดเป็น tangata whenua (ชนชาติของดินแดน) ของนิวซีแลนด์",
        "c_th": ["มาโอรี่", "ซามัวนเจอร์", "ฟิจีแลนด์", "โทนกา"]
    },
    {
        "num": 117,
        "q": "Which Ethiopian kingdom adopted Christianity early and has ancient manuscripts and rock-hewn churches?",
        "c": ["Aksum", "Kush", "Meroe", "Gondar"],
        "q_th": "อาณาจักรเอธิโอเปียใดรับเอาศาสนาคริสต์เร็วๆ และมีต้นฉบับโบราณและวิหารตัดหินสำเร็จ",
        "c_th": ["อักซุม", "กูช", "เมโรเอ", "กอนดาร์"]
    },
    {
        "num": 118,
        "q": "Which 19th-century rivalry between Britain and Russia for influence in Central Asia is called what?",
        "c": ["The Great Game", "The Silk Rivalry", "The Steppe Struggle", "The Khanate Wars"],
        "q_th": "การแข่งขันในศตวรรษที่ 19 ระหว่างอังกฤษและรัสเซีย เพื่อมีอิทธิพลในเอเชียกลางเรียกว่าอะไร",
        "c_th": ["เกมโลก", "การแข่งขันผ้าไหม", "การต่อสู้ของสตเป", "สงครามขาน"]
    },
    {
        "num": 119,
        "q": "Which English king was forced to sign the Magna Carta in 1215?",
        "c": ["King John", "King Henry II", "King Richard I", "King Stephen"],
        "q_th": "กษัตริย์อังกฤษองค์ใดถูกบังคับให้ลงนามในปริญญาเอกในปี 1215",
        "c_th": ["กษัตริย์จอห์น", "กษัตริย์เฮนรี่ที่สอง", "กษัตริย์ริชาร์ดที่หนึ่ง", "กษัตริย์สตีเฟน"]
    },
    {
        "num": 120,
        "q": "Which conference in 1864 helped lay the groundwork for Canadian Confederation in 1867?",
        "c": ["Charlottetown Conference", "Quebec Conference", "London Conference", "Ottawa Conference"],
        "q_th": "การประชุมใดในปี 1864 ช่วยสร้างความพร้อมสำหรับการสร้างสหพันธ์แคนาดาในปี 1867",
        "c_th": ["การประชุมชาร์ลอตเทาน์", "การประชุมควิเบก", "การประชุมลอนดอน", "การประชุมออตตาวา"]
    },
    {
        "num": 121,
        "q": "Which explorer discovered the New World in 1492 and sailed under the Spanish flag?",
        "c": ["Christopher Columbus", "Leif Erikson", "John Cabot", "Bartholomeu Dias"],
        "q_th": "นักสำรวจองค์ใดค้นพบโลกใหม่ในปี 1492 และแล่นเรือภายใต้ธงสเปน",
        "c_th": ["คริสโตเฟอร์ โคลัมบัส", "เลฟ เอริกสัน", "จอห์น คาบอต", "บาร์โธโลมิอู ดีแอส"]
    },
    {
        "num": 122,
        "q": "Which Italian Renaissance painter is famous for the Mona Lisa and anatomical studies?",
        "c": ["Leonardo da Vinci", "Michelangelo", "Botticelli", "Raphael"],
        "q_th": "จิตรกรยุคฟื้นฟูศิลปะอิตาลีองค์ใดโด่งดังในการวาดแมนโนลิซา และการศึกษาวิชาอนาโตมี่",
        "c_th": ["เลโอนาร์โด ดาวินชี", "มิเกเลแจโล", "บอตติเชลลี", "ราฟาเอล"]
    },
    {
        "num": 123,
        "q": "Which African country was never colonized by a European power and maintained its independence?",
        "c": ["Ethiopia", "Egypt", "Nigeria", "Sudan"],
        "q_th": "ประเทศแอฟริกาใดไม่เคยถูกปกครองระบบอาณานิคมโดยอำนาจยุโรป และรักษาอิสรภาพ",
        "c_th": ["เอธิโอเปีย", "อียิปต์", "ไนจีเรีย", "ซูดาน"]
    },
    {
        "num": 124,
        "q": "Which German political movement tried to unify German-speaking peoples in the 19th century?",
        "c": ["Pan-Germanism", "Romanticism", "Liberalism", "Nationalism"],
        "q_th": "ขบวนการทางการเมืองเยอรมันใดพยายามสร้างความสามัคคีให้กับชนชาติพูดภาษาเยอรมันในศตวรรษที่ 19",
        "c_th": ["แพนเยอรมันนิสม์", "โรแมนติกนิสม์", "เสรีนิยม", "ชาตินิยม"]
    },
    {
        "num": 125,
        "q": "Which revolution overthrew the Qing Dynasty in China and established the Republic of China?",
        "c": ["Chinese Revolution of 1911", "Boxer Rebellion", "Taiping Rebellion", "Chinese Civil War"],
        "q_th": "การปฏิวัติใดจึงโค่นล้มราชวงศ์ฉิงในจีน และสร้างสาธารณรัฐจีน",
        "c_th": ["การปฏิวัติจีนปี 1911", "การกบฏขอหมวด", "การกบฏไท่เป่ง", "สงครามกลางเมืองจีน"]
    },
    {
        "num": 126,
        "q": "Which Pacific Island group is considered the center of Polynesian culture?",
        "c": ["Hawaii", "Samoa", "Tonga", "Tahiti"],
        "q_th": "กลุ่มเกาะแปซิฟิกใดถูกพิจารณาว่าเป็นศูนย์กลางของวัฒนธรรมโพลิเนเซีย",
        "c_th": ["ฮาวาย", "ซามัวร์", "โตนกา", "ตาฮีตี"]
    },
    {
        "num": 127,
        "q": "Which South American country is the largest by area and borders every other South American nation except Chile and Ecuador?",
        "c": ["Brazil", "Argentina", "Peru", "Colombia"],
        "q_th": "ประเทศอเมริกาใต้ใดมีพื้นที่ใหญ่ที่สุด และติดต่อชายแดนกับประเทศอเมริกาใต้อื่นๆ ยกเว้นชิลี และเอกวาดอร์",
        "c_th": ["บราซิล", "อาร์เจนติน่า", "เปรู", "โคลอมเบีย"]
    },
    {
        "num": 128,
        "q": "Which famous archaeologist discovered the tomb of Tutankhamun in Egypt?",
        "c": ["Howard Carter", "Flinders Petrie", "Auguste Mariette", "Émile Brugsch"],
        "q_th": "นักโบราณคดีที่มีชื่อเสียงองค์ใดค้นพบสุสานของทุตันคามูนในอียิปต์",
        "c_th": ["โฮวาร์ด คาร์เตอร์", "ฟลินเดอร์ส เพทรี", "ออกุสต์ มาเรียต", "เอมีล บรูจช์"]
    },
    {
        "num": 129,
        "q": "Which North American indigenous confederacy was formed in the Great Lakes region and influenced the U.S. Constitution?",
        "c": ["Iroquois Confederacy", "Powhatan Confederacy", "Natchez Confederation", "Creek Confederacy"],
        "q_th": "สหพันธ์อเมริกาเหนือชนพื้นเมืองใดก่อตั้งขึ้นในเขตมหาสระอเกรต และมีอิทธิพลต่อรัฐธรรมนูญสหรัฐฯ",
        "c_th": ["สหพันธ์อิโรควอย", "สหพันธ์พอวาตัน", "สหพันธ์นาชเชส", "สหพันธ์ครีก"]
    },
    {
        "num": 130,
        "q": "Which region in the Middle East was the center of ancient Mesopotamian civilization?",
        "c": ["Between the Tigris and Euphrates rivers", "Nile River valley", "Arabian Peninsula", "Levant"],
        "q_th": "ภูมิภาคใดในตะวันออกกลางเป็นศูนย์กลางของอารยธรรมเมโสโปเตเมีย",
        "c_th": ["ระหว่างแม่น้ำไทกริสและยูเฟรตส์", "หุบเขาแม่น้ำไนล์", "คาบสมุทรอาหรับ", "เลวานต์"]
    },
    {
        "num": 131,
        "q": "Which Indus Valley civilization flourished around 2600–1900 BCE and had cities like Harappa and Mohenjo-daro?",
        "c": ["Indus Valley Civilization", "Aryan Civilization", "Vedic Civilization", "Mauryan Civilization"],
        "q_th": "อารยธรรมหุบเขาสินธุใดเจริญรุ่งเรืองประมาณ 2600-1900 ปีก่อนคริสตศักราช และมีเมืองเช่นหารัปปา และโมเฮนโจดาโร",
        "c_th": ["อารยธรรมหุบเขาสินธุ", "อารยธรรมอาเรีย", "อารยธรรมเวทย์", "อารยธรรมเมาร์ยัน"]
    },
    {
        "num": 132,
        "q": "Which European power first established a permanent trading post in India at Goa in 1510?",
        "c": ["Portugal", "Spain", "France", "Britain"],
        "q_th": "อำนาจยุโรปใดก่อตั้งสถานีค้าถาวรแรกในอินเดีย ที่โกอา ในปี 1510",
        "c_th": ["โปรตุเกส", "สเปน", "ฝรั่งเศส", "อังกฤษ"]
    }
]

# Output as JSON array
print(json.dumps(questions_data, ensure_ascii=False, indent=2))
