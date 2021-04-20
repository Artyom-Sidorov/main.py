import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from Config import TOKEN
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Test(StatesGroup):
    Name = State()
    Data = State()
    City = State()
    Number = State()
    Prof = State()


@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await bot.send_message(message.chat.id, "«Колледж «Туран» — образовательное учреждение, основанное в 2000 году, "
                                            "работает в системе непрерывного образования «колледж-ВУЗ» совместно с "
                                            "университетом «Туран» г. Алматы, с университетом «Туран-Астана». Общая "
                                            "численность составляет 1 200 студентов. За восемнадцать лет работы "
                                            "учебным заведением выпущено более пяти тысяч студентов.По окончании "
                                            "колледжа «Туран» выдается диплом государственного образца, на основании "
                                            "которого выпускники могут продолжить образование в ВУЗах Казахстана и за "
                                            "рубежом по родственным специальностям с сокращенным сроком обучения. "
                                            "Колледж осуществляет деятельность в сфере технического и "
                                            "профессионального образования в соответствии с государственной лицензией "
                                            "(KZ1LAA00006433 от 20 января 2016 г.) по специальностям, востребованными "
                                            "на рынке труда")


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Для студентов")
    button_2 = types.KeyboardButton(text="Для абитурентов")
    button_3 = types.KeyboardButton(text="Контакты")
    keyboard.add(button_1, button_2, button_3)
    await bot.send_message(message.chat.id, "Выберете пункт", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Контакты")
async def con(message: types.Message):
    await bot.send_message(message.chat.id, "КОНТАКТНАЯ ИНФОРМАЦИЯ: \nул. Александра Бараева 9/2, 010000 Астана, "
                                            "Казахстан,\nПриемная комиссия  +7 776 143 61 71\nПриемная директора  +7 ("
                                            "7172) 202 009\nСтуденческий отдел  +7 (7172) 202 004\nKol.turan@mail.ru")


@dp.message_handler(lambda message: message.text == "Для студентов")
async def student(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Рассписание")
    button_2 = types.KeyboardButton(text="График экзаменов")
    button_3 = types.KeyboardButton(text="Практика студентов")
    keyboard.add(button_1, button_2, button_3)
    await bot.send_message(message.chat.id, "Выберете пункт", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Рассписание")
async def schedule(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Первый курс", callback_data="One"),
                 types.InlineKeyboardButton(text="Второй курс", callback_data="Two"),
                 types.InlineKeyboardButton(text="Третий курс", callback_data="Three"),
                 types.InlineKeyboardButton(text="Четвертый курс", callback_data="Four"))
    await bot.send_message(message.chat.id, "Выберете курс", reply_markup=keyboard)


@dp.callback_query_handler(text="One")
async def one(call: types.CallbackQuery):
    await call.message.reply("https://college-turan.kz/6984-2/")


@dp.callback_query_handler(text="Two")
async def one(call: types.CallbackQuery):
    await call.message.reply("https://college-turan.kz/raspisanie2/")


@dp.callback_query_handler(text="Three")
async def one(call: types.CallbackQuery):
    await call.message.reply("https://college-turan.kz/raspisanie3/")


@dp.callback_query_handler(text="Four")
async def one(call: types.CallbackQuery):
    await call.message.reply(
        "https://college-turan.kz/%d1%80%d0%b0%d1%81%d0%bf%d0%b8%d1%81%d0%b0%d0%bd%d0%b8%d0%b5-4"
        "-%d0%ba%d1%83%d1%80%d1%81/")


@dp.message_handler(lambda message: message.text == "График экзаменов")
async def exam(message: types.Message):
    await bot.send_message(message.chat.id, "https://college-turan.kz/grafik-2020/")


@dp.message_handler(lambda message: message.text == "Практика студентов")
async def schedule(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="АРХИТЕКТУРА", callback_data="ARCHITECTURE"),
                 types.InlineKeyboardButton(text="ТУРИЗМ", callback_data="TOURISM"),
                 types.InlineKeyboardButton(text="ДИЗАЙН", callback_data="DESIGN"),
                 types.InlineKeyboardButton(text="МЕНЕДЖМЕНТ", callback_data="MANAGEMENT"),
                 types.InlineKeyboardButton(text="ФИНАНСЫ", callback_data="FINANCE"),
                 types.InlineKeyboardButton(text="УЧЕТ И АУДИТ", callback_data="ACCOUNTING AND AUDITING"),
                 types.InlineKeyboardButton(text="ПРАВОВЕДЕНИЕ", callback_data="JURISPRUDENCE"),
                 types.InlineKeyboardButton(text="ИНФОРМАЦИОННЫЕ СИСТЕМЫ", callback_data="INFORMATION SYSTEMS"),
                 types.InlineKeyboardButton(text="ВЫЧИСЛИТЕЛЬНАЯ ТЕХНИКА И ПО", callback_data="COMPUTER EQUIPMENT AND "
                                                                                              "SOFTWARE", ),
                 types.InlineKeyboardButton(text="ОРГАНИЗАЦИЯ ОБСЛУЖИВАНИЯ ГОСТИНИЧНЫХ ХОЗЯЙСТВ",
                                            callback_data="OOSOH"))

    await bot.send_message(message.chat.id, "Выберете направление", reply_markup=keyboard)


@dp.callback_query_handler(text="ARCHITECTURE")
async def ARCHITECTURE(call: types.CallbackQuery):
    await call.message.reply(">НИПИ «Астана Генплан» \n >ГУ «Отдел архитектуры и "
                             "градостроительства» \n >ТОО « Астана "
                             "Құрылыс» \n >Акционерное общество «Астана-Өнім» \n >ТОО «Алтын кереге құрылыс монтаж» "
                             "\n >ТОО «Астана –Қөркем» \n >ТОО «Астана-Профи» \n >ТОО «Жас кұрылыс АСТ» \n >ТОО "
                             "«АКТ-Проект»")


@dp.callback_query_handler(text="TOURISM")
async def TOURISM(call: types.CallbackQuery):
    await call.message.reply(
        ">«IBIS HOTEL ASTANA» \n >Тур.агенство «Triumph-travel» \n >Тур.агенство «Aknur-travel» "
        "\n >Тур.агенство «Satti-travel» \n >Тур.агенство «Горизонт» \n >ТОО «Тан-тур» \n >ТОО "
        "«Sun tour Astana» \n >Гостинично-ресторанный комплекс «G-Empire» \n >«Comfort hotel "
        "Astana» \n >Гостиница «Мукаммаль» \n >Гостиница «Жасамир»")


@dp.callback_query_handler(text="DESIGN")
async def DESIGN(call: types.CallbackQuery):
    await call.message.reply(">НИПИ «Астана Генплан»город Астана \n >ГУ «Отдел архитектуры и градостроительства» "
                             "г.Астаны \n >ТОО « Астана Құрылыс» \n >Акционерное общество «Астана-Өнім» "
                             "\n >ТОО «Астана –Қөркем» \n >ТОО «АКТ-Проект» \n >ИП «Нуржауган» швейный салон")


@dp.callback_query_handler(text="MANAGEMENT")
async def MANAGEMENT(call: types.CallbackQuery):
    await call.message.reply(">Национальная палата предпринимателей «Атамекен» \n >АО «КазТрансГаз Аймак» \n >АО "
                             "«Национальный научный медицинский центр» \n >ТОО «Логитекс» \n >АО «Республиканский "
                             "научно-методический центр развития технического и профессионального образования и "
                             "присвоения квалификации»")


@dp.callback_query_handler(text="OOSOH")
async def OOSOH(call: types.CallbackQuery):
    await call.message.reply(">Гостинично-ресторанный комплекс «G-Empire» \n >«Comfort hotel Astana» \n >Гостиница "
                             "«Мукаммаль» \n >Гостиница «Жасамир» \n >Гостиница «Rixos»")


@dp.callback_query_handler(text="FINANCE")
async def FINANCE(call: types.CallbackQuery):
    await call.message.reply(">ТОО «Аксиома» \n >Национальная палата предпринимателей «Атамекен» \n >ТОО «Ақ жол "
                             "қалқама» \n >ТОО «Астана LRT» \n >ТОО «Бай Шатыр» \n >Строительная компания "
                             "«BI-Group» "
                             "\n >АО «Альфа-банк» \n >Банк «Каssa-Nova» \n >Филиал АО «Азия Кредит Банк»")


@dp.callback_query_handler(text="ACCOUNTING AND AUDITING")
async def ACCOUNTING_AND_AUDITING(call: types.CallbackQuery):
    await call.message.reply(">ТОО «Аксиома» \n >Национальная палата предпринимателей «Атамекен» \n >ТОО «Ақ жол "
                             "қалқама» \n >ТОО «Астана LRT» \n >ТОО «Бай Шатыр» \n >Строительная компания "
                             "«BI-Group» "
                             "\n >АО «Альфа-банк» \n >Банк «Каssa-Nova» \n >Филиал АО «Азия Кредит Банк»")


@dp.callback_query_handler(text="JURISPRUDENCE")
async def JURISPRUDENCE(call: types.CallbackQuery):
    await call.message.reply(">Специализированный экономический суд \n >Алматинский районый суд \n >Администратор "
                             "судов \n >Сарыаркинский военкомат \n >АО «Казпочта» \n >Специализированный "
                             "межрайонный "
                             "военный суд по уголовным делам \n >ГУ «Канцелярия суда» \n >Алматинский военкомат \n "
                             ">Национальная палата предпринимателей «Атамекен» ")


@dp.callback_query_handler(text="INFORMATION SYSTEMS")
async def INFORMATION_SYSTEMS(call: types.CallbackQuery):
    await call.message.reply(">АО «Национальный научный медицинский центр» \n >АО «Республиканский "
                             "научно-методический центр развития технического и профессионального образования и "
                             "присвоения квалификации» \n >ТОО «Panorama LLP» \n >ТОО «Lane Company» \n >ТОО "
                             "«TechSoft» \n >АО «КазТрансГаз Аймак» \n >ТОО «Логитекс» \n >АО «Казпочта» \n "
                             ">Сервисный центр «Белый ветер» \n >ТОО «Планета компьютеров» \n >ТОО «HanAli» "
                             "AT-компания")


@dp.callback_query_handler(text="COMPUTER EQUIPMENT AND SOFTWARE")
async def COMPUTER_EQUIPMENT_AND_SOFTWARE(call: types.CallbackQuery):
    await call.message.reply(">АО «Национальный научный медицинский центр» \n >АО «Республиканский "
                             "научно-методический центр развития технического и профессионального образования и "
                             "присвоения квалификации» \n >ТОО «Panorama LLP» \n >ТОО «Lane Company» \n >ТОО "
                             "«TechSoft» \n >АО «КазТрансГаз Аймак» \n >ТОО «Логитекс» \n >АО «Казпочта» \n "
                             ">Сервисный центр «Белый ветер» \n >ТОО «Планета компьютеров» \n >ТОО «HanAli» "
                             "AT-компания")


@dp.message_handler(lambda message: message.text == "Для абитурентов")
async def entrants(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text='Наши специальности'),
                 types.KeyboardButton(text='Правила приема документов'),
                 types.KeyboardButton(text='Прием документов'))
    await bot.send_message(message.chat.id, "Выберете пункт", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Наши специальности")
async def entrants(message: types.Message):
    await bot.send_message(message.chat.id, "Менеджмент:\nНаука об эффективном управлении предприятием, организации "
                                            "предприятия о "
                                            "стратегии его развития.\n Финансы:\nФинансы - это не денежные средства, "
                                            "а отношения по "
                                            "поводу образования и использования фондов денежных "
                                            "средств.\nТуризм:\nТуризм сегодня – это "
                                            "динамично развивающаяся отрасль экономики.\nПравоведение:\nВладение "
                                            "основами гуманитарных "
                                            "и "
                                            "социально-экономических наук, знание основ Конституции "
                                            "РК.\nИнформационные "
                                            "системы:\nФинансово-кредитная информация в информационных системах; "
                                            "техническая "
                                            "информация.\nВТ и ПО:\nПрограммирования, построения и администрирования "
                                            "ИС и сетей, "
                                            "создания и управления БД.\nОбслуживание гост.хоз.:\nОбъектом "
                                            "профессиональной деятельности "
                                            "менеджера является гостиничное предприятие.\nДизайн:\nДизайн - проектная "
                                            "художественно- "
                                            "техническая деятельность\nУчет и аудит:\nНесмотря на то, что бухгалтеров "
                                            "на рынке труда "
                                            "много, поиск иной раз занимает целые "
                                            "месяцы.\nАрхитектура:\nТехник-проектировщик, "
                                            "проектирует здания и сооружения; жилые дома, офисы и т.д\n"
                                            "Больше информации на сайте: https://college-turan.kz/spetsialnosti/")


@dp.message_handler(lambda message: message.text == 'Правила приема документов')
async def doc(messgae: types.Message):
    await bot.send_message(messgae.chat.id, "https://college-turan.kz/pravila-priyema/")


@dp.message_handler(lambda message: message.text == 'Прием документов', state=None)
async def doc(messgae: types.Message):
    await messgae.answer("Имя и Фамилия")
    await Test.Name.set()


@dp.message_handler(state=Test.Name)
async def name(message: types.Message, state: FSMContext):
    global Name
    Name = message.text
    await state.update_data(answer1=Name)
    await message.answer("Дата рождения(формат: 00д/00м/0000г)")
    await Test.next()


@dp.message_handler(state=Test.Data)
async def data(message: types.Message, state: FSMContext):
    global Data
    Data = message.text
    await state.update_data(answer2=Data)
    await message.answer("Ваш город")
    await Test.next()


@dp.message_handler(state=Test.City)
async def city(message: types.Message, state: FSMContext):
    global City
    City = message.text
    await state.update_data(answer3=City)
    await message.answer("Ваш номер телефона для связи")
    await Test.next()


@dp.message_handler(state=Test.Number)
async def number(message: types.Message, state: FSMContext):
    global Number
    Number = message.text
    await state.update_data(answer4=Number)
    await message.answer("На какую специальность вы хотите поступить?")
    await Test.next()


@dp.message_handler(state=Test.Prof)
async def number(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("Number")
    global Prof
    Prof = message.text
    await message.answer("Спасибо, ваша заявка отправлена")
    await state.reset_state()
    spam()


def spam():
    to_email = 'artemych.81@mail.ru'
    message = "Абитурент: " + Name + "\n" + "Дата рождения: " + Data + "\n" + "Телефон: " + Number + "\n" + "Гоород: " \
              + City + "\n" + "Направление: " + Prof
    topic = "Заявка"
    from_email = 'artemych.81@mail.ru'
    password = 'Art19012001em'
    msg = MIMEMultipart()
    msg['Subject'] = topic
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.mail.ru: 25')
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Не понимаю вас")


if __name__ == "__main__":
    executor.start_polling(dp)
