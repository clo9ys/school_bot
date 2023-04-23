from templates import *

BOT_TOKEN = "its a token"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


reply_keyboard = [['/help'], ['/lessons', '/work'],
                  ['/school', '/school_site']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


async def start(update, context):
    await update.message.reply_text(
        "Я бот-справочник школы.\n"
        "\n"
        "Вот все мои навыки:\n"
        "/school - Как записать ребенка в нашу школу\n"
        "/work - Как устроиться на работу в школу\n"
        "/school_site - Сайт школы\n"
        "/lessons - Внеурочные занятия и секции\n"
        "\n"
        "Какая информация вам нужна?",
        reply_markup=markup
    )


async def help_command(update, context):
    await update.message.reply_text("Вот все мои навыки:\n"
                                    "/school - Как записать ребенка в нашу школу\n"
                                    "/work - Как устроиться на работу в школу\n"
                                    "/school_site - Сайт школы\n"
                                    "/lessons - Внеурочные занятия и секции")


async def school_site(update, context):
    await update.message.reply_text("Более подробно узнать о нашей школе можете узнать на нашем сайте :\n"
                                    "https://not/ready/site/3454\n"
                                    "(в данный момент сайт находится в разработке)")


async def lessons(update, context):
    await update.message.reply_text("Если вам тяжело выбрать секцию, то\n"
                                    "Для более качественного подбора предлагаю вам пройти опрос \n"
                                    "Отвечайте 'Да' или 'Нет'")

    return 1


async def first_response(update, context):
    # Это ответ на первый вопрос.
    # Мы можем использовать его во втором вопросе.
    locality = update.message.text
    if locality.lower() == 'да':
        await update.message.reply_text(
            f"Для выхода из опроса напишите команду /stop\n"
            f"Ваш ребенок любит спорт?")
        return 2
    if locality.lower() == 'нет':
        await update.message.reply_text("Всего доброго!")
        return ConversationHandler.END
    else:
        await update.message.reply_text('Ваш ответ некорректный,\n'
                                        'Попробуйте еще раз')


async def second_response(update, context):
    # Ответ на второй вопрос.
    # Мы можем его сохранить в базе данных или переслать куда-либо.
    answer = update.message.text
    logger.info(answer)
    if answer.lower() == 'да':
        await update.message.reply_text("Укажите вид спорта, которым ваш ребенок желает заниматься.")
        return 3
    if answer.lower() == 'нет':
        await update.message.reply_text("Возможно ваш ребенок любит робототехнику и программирование?")
        return 4
    else:
        await update.message.reply_text('Ваш ответ некорректный,\n'
                                        'Попробуйте еще раз')


async def third_response(update, context):
    answer2 = update.message.text
    logger.info(answer2)
    if answer2.lower() == 'футбол':
        await update.message.reply_text('Расписание занятий:\n'
                                        'Пн - 16:30-18:30\n'
                                        'Ср - 14:30-16:30\n'
                                        'Пт - 16:30-18:30')
        return ConversationHandler.END

    if answer2.lower() == 'волейбол':
        await update.message.reply_text('Расписание занятий:\n'
                                        'Вт - 16:30-18:30\n'
                                        'Чт - 14:30-16:30\n'
                                        'Сб - 16:30-18:30')
        return ConversationHandler.END

    if answer2.lower() == 'баскетбол':
        await update.message.reply_text('Расписание занятий:\n'
                                        'Пн - 14:30-16:30\n'
                                        'Ср - 16:30-18:30\n'
                                        'Пт - 14:30-16:30')
        return ConversationHandler.END

    if answer2.lower() == 'хоккей':
        await update.message.reply_text('Расписание занятий:\n'
                                        'Вт - 14:30-16:30\n'
                                        'Чт - 16:30-18:30\n'
                                        'Сб - 14:30-16:30')
        return ConversationHandler.END

    else:
        await update.message.reply_text('Ваш ответ некорректный или в нашей школе нет данного вида спорта,\n'
                                        'Попробуйте еще раз')


async def fourth_response(update, context):
    answer3 = update.message.text
    logger.info(answer3)
    if answer3.lower() == 'да':
        await update.message.reply_text('Выберите одну из секций.')

    if answer3.lower() == 'нет':
        await update.message.reply_text('Больше мне нечего вам предложить из нашего списка секций.')

    else:
        await update.message.reply_text('Ваш ответ некорректный,\n'
                                        'Попробуйте еще раз')


async def double_fourth_response(update, context):
    answer44 = update.message.text
    logger.info(answer44)
    if answer44.lower() == 'программирование':
        await update.message.reply_text('Расписание занятий:\n'
                                        'Вт - 14:30-16:30\n'
                                        'Чт - 16:30-18:30\n'
                                        'Сб - 14:30-16:30')
        return ConversationHandler.END

    if answer44.lower() == 'робототехника':
        await update.message.reply_text('Расписание занятий:\n'
                                        'Пн - 14:30-16:30\n'
                                        'Ср - 16:30-18:30\n'
                                        'Пт - 14:30-16:30')
        return ConversationHandler.END
    else:
        await update.message.reply_text('Ваш ответ некорректный,\n'
                                        'Попробуйте еще раз')


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


async def work(update, context):
    await update.message.reply_text('Если вы хотите устроиться работать в нашу школу,\n'
                                    'Но не можете определиться с выбором должности,\n'
                                    'То предлагаю пройти опрос\n'
                                    '\n'
                                    'Отвечайте "да" или "нет"')
    return 5


async def fifth_response(update, context):
    answer5 = update.message.text
    logger.info(answer5)

    if answer5.lower() == 'да':
        await update.message.reply_text("Для выхода из опроса напишите команду /stop \n"
                                        "\n"
                                        "Вы хотите быть учителем?")
        return 6

    if answer5.lower() == 'нет':

        await update.message.reply_text("Всего доброго!")
        return ConversationHandler.END

    else:
        await update.message.reply_text('Ваш ответ некорректный,\n'
                                        'Попробуйте еще раз')


async def sixth_response(update, context):
    answer6 = update.message.text
    logger.info(answer6)

    if answer6.lower() == 'да':
        await update.message.reply_text('Вы бы хотели преподовать какие-либо науки?')
        return 7

    if answer6.lower() == 'нет':
        await update.message.reply_text('Вы бы хотели работать в администрации школы?')
        return 10

    else:
        await update.message.reply_text('Ваш ответ некорректный,\n'
                                        'Попробуйте еще раз')


async def seventh_response(update, context):
    answer7 = update.message.text
    logger.info(answer7)

    if answer7.lower() == 'да':
        await update.message.reply_text('Какую науку вы бы хотели преподавать?')
        return 9

    if answer7.lower() == 'нет':
        await update.message.reply_text('Возможно вы хотите быть учителем иностранных или русского языков?')
        return 10

    else:
        await update.message.reply_text('Ваш ответ некорректный,\n'
                                        'Попробуйте еще раз')


async def ninth_response(update, context):
    answer9 = update.message.text
    logger.info(answer9)

    if answer9.lower() == 'математика':
        await update.message.reply_text("Отлично, вы записаны на собеседование,\n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    if answer9.lower() == 'физика':
        await update.message.reply_text("Отлично, вы записаны на собеседование,\n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    if answer9.lower() == 'информатика':
        await update.message.reply_text("Отлично, вы записаны на собеседование,\n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    if answer9.lower() == 'биология':
        await update.message.reply_text("Отлично, вы записаны на собеседование,\n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    if answer9.lower() == 'география':
        await update.message.reply_text("Отлично, вы записаны на собеседование,\n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    if answer9.lower() == 'история':
        await update.message.reply_text("Отлично, вы записаны на собеседование,\n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    if answer9.lower() == 'химия':
        await update.message.reply_text("Отлично, вы записаны на собеседование,\n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    if answer9.lower() == 'литература':
        await update.message.reply_text("Отлично, вы записаны на собеседование,\n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    if answer9.lower() == 'обществознание':
        await update.message.reply_text("Отлично, вы записаны на собеседование,\n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    else:
        await update.message.reply_text('Ваш ответ некорректный или данного предмета нет в нашей школе,\n'
                                        'Попробуйте еще раз')


async def tenth_response(update, context):
    answer8 = update.message.text
    logger.info(answer8)

    if answer8.lower() == 'да':
        await update.message.reply_text("Отлично, вы записаны на собеседование, \n"
                                        "В скором времени с вами свяжутся")
        return ConversationHandler.END

    if answer8.lower() == 'нет':
        await update.message.reply_text("Жаль, что я не помог вам,\n"
                                        " но вы можете узнать больше о профессиях в нашей школе,\n"
                                        " Позвонив по номеру: +7(915)677-2023")
        return ConversationHandler.END

    else:
        await update.message.reply_text('Ваш ответ некорректный,\n'
                                        'Попробуйте еще раз')


async def school(update, context):
    await update.message.reply_text("Вы хотите записать своего ребенка в нашу школу?")
    return 12


async def twelfth_response(update, context):
    answer = update.message.text
    logger.info(answer)
    if answer.lower() == 'да':
        await update.message.reply_text('В каком классе учится ваш ребенок?')
        return 13

    if answer.lower() == 'нет':
        await update.message.reply_text('Очень жаль.')
        return ConversationHandler.END

    else:
        await update.message.reply_text('Ваш ответ некорректный,\n'
                                        'Попробуйте еще раз')


async def thirteenth_response(update, context):
    answer = update.message.text
    logger.info(answer)
    cls = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З"]
    await update.message.reply_text(f'Прекрасно, ваш ребенок записан в класс {str(answer) + random.choice(cls)}, \n'
                                    f'С вами обязательно свяжутся.')
    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("school_site", school_site))

    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('lessons', lessons)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_response)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, third_response)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, fourth_response)],
            44: [MessageHandler(filters.TEXT & ~filters.COMMAND, double_fourth_response)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler)

    conv_handler2 = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('work', work)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, fifth_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, sixth_response)],
            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, seventh_response)],
            9: [MessageHandler(filters.TEXT & ~filters.COMMAND, ninth_response)],
            10: [MessageHandler(filters.TEXT & ~filters.COMMAND, tenth_response)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler2)

    conv_handler3 = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('school', school)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            12: [MessageHandler(filters.TEXT & ~filters.COMMAND, twelfth_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            13: [MessageHandler(filters.TEXT & ~filters.COMMAND, thirteenth_response)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler3)

    application.run_polling()


if __name__ == '__main__':
    main()
