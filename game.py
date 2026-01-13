def battle(player, threat):
    print(f"⚔️ БІЙ ЗАГРОЗИ: {threat['name']}")
    player['hope'] -= threat['power']
    print(f"Надія зменшилась на {threat['power']}")
def create_character():
    print('❄️ СТВОРЕННЯ ПЕРСОНАЖА ❄️')
    name = input('Введіть імʼя Капітана: ').strip()
    if name == '':
        name = 'Безіменний Капітан'
    player = {
        'name': name,
        'day': 1,
        'temp': -20,
        'hope': 50,
        'discontent': 20,
        'trust': 50,
        'people': 50,
        'sick': 5,
        'coal': 100,
        'food': 80,
        'wood': 60,
        'steel': 40,
        'laws': [
            'Подвійні зміни',
            'Дитяча праця',
            'Суп з тирсою',
            'Молитовний дім',
            'Кара за крадіжку'
        ],
        'laws_state': [0, 0, 0, 0, 0],
        'events': [
            'Буря наближається',
            'Хвороба поширюється',
            'Знайдено покинуте селище',
            'Протест робітників',
            'Надія зростає'
        ],
        'generator_level': 1,
        'houses': 5,
        'medical_post': 1,
        'workshops': 0,
        'scouts_sent': 0,
        'ultimatum': -1,
        'great_storm': 0,
        'factions': ['Робітники', 'Інженери', 'Віруючі'],
        'factions_trust': [50, 50, 50],
        'ideology': 0,
        'ideology_name': 'не вибрана',
        'leader_alive': 1,
        'rumors': 0,
        'newspaper_trust': 50,
        'newspaper_titles': [
            'ГЕНЕРАТОР - СЕРЦЕ МІСТА',
            'ЛЮДИ НА МЕЖІ',
            'ХОЛОД ПОСИЛЮЄТЬСЯ',
            'РІШЕННЯ КАПІТАНА',
            'НАДІЯ ЩЕ ЖИВА'
        ],
        'newspaper_articles': [
            'Генератор працює без зупину. Він дає місту шанс.',
            'Невдоволення зростає. Люди вимагають змін.',
            'Мороз стає нестерпним навіть у домівках.',
            'Капітан приймає важкі рішення для виживання',
            'Попри все, місто не здається.'
        ],
        'dilema': [0, 0, 0]
    }
    print(f'\nЛаскаво просимо, Капітане {name}!\n')
    threat = {
    'name': 'Великий холод',
    'power': 3
    }
    battle(player, threat)
    return player
def show_status(player):
    print('\n📊 СТАН МІСТА')
    print('-' * 30)
    print(f"👤 Капітан: {player['name']}")
    print(f"📅 День: {player['day']}")
    print(f"🌡 Температура: {player['temp']}°C")
    print()
    print(f"🔥 Вугілля: {player['coal']}")
    print(f"🍞 Їжа: {player['food']}")
    print(f"🪵 Дерево: {player['wood']}")
    print(f"🔩 Сталь: {player['steel']}")
    print()
    print(f"👥 Люди: {player['people']}")
    print(f"🤒 Хворі: {player['sick']}")
    print()
    print(f"✨ Надія: {player['hope']}")
    print(f"😠 Невдоволення: {player['discontent']}")
    print(f"🤝 Довіра: {player['trust']}")
    print('-' * 30)
def player_action(player):
    print('Обери дію:')
    print('1 - Відправити людей працювати')
    print('2 - Лікування хворих')
    if 0 in player['laws_state']:
        print('3 - Прийняти закон')
    print('4 - Керування генератором')
    print('5 - Побудувати будівлю')
    print('6 - Відправити розвідників')
    if player['ideology'] == 0:
        print('7 - Обрати ідеологію міста')
    print('8 - Вплинути на газету')
    print('9 - Нічого не робити')
    choice = input('> ')
    return choice
def safe_input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f'❌ Введіть число не менше {min_val}')
                continue
            if max_val is not None and value > max_val:
                print(f'❌ Введіть число не більше {max_val}')
                continue
            return value
        except ValueError:
            print('❌ Помилка: потрібно ввести число!')
print('❄️ FROSTPUNK: ОСТАННЄ МІСТО ❄️')
print('Світ замерз. Ти - Капітан. Від твоїх рішень залежить життя міста. \n')
player = create_character()
while player['people'] > 0 and player['hope'] > 0 and player['day'] <= 30:
    show_status(player)
    player['coal'] -= player['people'] // 3
    player['food'] -= player['people'] // 3
    if player['coal'] < 0:
        player['coal'] = 0
        player['hope'] -= 5
        player['discontent'] += 10
        print('Місто мерзне! Не вистачає вугілля.\n')
    if player['food'] < 0:
        player['food'] = 0
        player['hope'] -= 10
        player['sick'] += 3
        print('Голод у місті! Люди слабшають.\n')
    if player['day'] == 25:
        print('❄️ ❄️ ❄️ ПОПЕРЕДЖЕННЯ ❄️ ❄️ ❄️')
        print('Розвідники повідомляють: наближається Велика Буря')
        print('Місто має підготуватися...')
    if player['day'] >= 26:
        if player['great_storm'] == 0:
            print('🌪️ ВЕЛИКА БУРЯ ПОЧАЛАСЯ 🌪️')
            player['great_storm'] = 1
        player['temp'] -= 5
        player['coal'] -= player['people'] // 2
        player['hope'] -= 3
        player['sick'] += 2
        print(f"Температура впала до {player['temp']}")
        print('Буря пожирає вугілля і сили людей.')
        if player['generator_level'] < 2:
            player['sick'] += 3
            player['hope'] -= 5
            print('Генератор занадто слабкий!')
    event_id = player['day'] % 5
    print(f"Подія: {player['events'][event_id]}")
    if event_id == 0:
        player['temp'] -= 5
        player['hope'] -= 5
        print('Температура різко впала.\n')
    if event_id == 1:
        player['sick'] += 2
        player['hope'] -= 3
        print('Збільшилася кількість хворих.\n')
    if event_id == 2:
        player['wood'] += 20
        player['steel'] += 10
        print('Розвідники принесли ресурси.\n')
    if event_id == 3:
        player['discontent'] += 5
        player['hope'] -= 2
        print('Люди незадоволені важкими умовами.\n')
    if event_id == 4:
        player['hope'] += 4
        print('Люди вірять у майбутнє.\n')
    player['news_id'] = player['day'] % 5
    print('📰 ГАЗЕТА МІСТА')
    print(player['newspaper_titles'][player['news_id']])
    print(f"{player['newspaper_articles'][player['news_id']]} \n")
    if player['hope'] < 20:
        print('Газета пише про страх і відчай. \n')
        player['newspaper_trust'] -= 5
        player['discontent'] += 2
    if player['discontent'] > 60:
        print('Газета попереджає про можливі заворушення. \n')
        player['newspaper_trust'] -= 5
    if player['hope'] > 60:
        print('Газета надихає людей не здаватися. \n')
        player['newspaper_trust'] += 5
    if player['newspaper_trust'] < 0:
        player['newspaper_trust'] = 0
    if player['newspaper_trust'] > 100:
        player['newspaper_trust'] = 100
    if player['day'] == 7 and player['dilema'][0] == 0:
        player['dilema'][0] = 1
        print('⚖️ МОРАЛЬНА ДИЛЕМА')
        print('Діти мерзнуть у холодних будинках.')
        print('1 - Відправити людей працювати')
        print('2 - Захистити дітей')
        d = safe_input_int('> ', 1, 2)
        if d == 1:
            player['food'] += 15
            player['coal'] += 10
            player['hope'] -= 10
            player['discontent'] += 5
            print('Діти працюють. Місто отримало ресурси.')
            print('Але люди не забудуть цього рішення.')
        if d == 2:
            player['hope'] += 10
            player['food'] -= 10
            print('Діти захищені.')
            print('Місто слабше, але людяність збережена.')
    if player['day'] == 14 and player['dilema'][1] == 0:
        player['dilema'][1] = 1
        print('⚖️ МОРАЛЬНА ДИЛЕМА')
        print('Ліків не вистачає на всіх.')
        print('1 - Лікувати робітників')
        print('2 - Лікувати слабких')
        d = safe_input_int('> ', 1, 2)
        if d == 1:
            player['sick'] -= 3
            player['hope'] -= 5
            player['discontent'] += 3
            print('Робітники врятовані.')
            print('Місто фунціонує, але люди обурені.')
        if d == 2:
            player['sick'] -= 2
            player['hope'] += 8
            player['food'] -= 5
            print('Слабких врятовано.')
            print('Люди вдячні, але ресурси витрачені.')
    if player['day'] == 21 and player['dilema'][2] == 0:
        player['dilema'][2] = 1
        print('⚖️ МОРАЛЬНА ДИЛЕМА')
        print('Розвідники дізналися страшну правду про бурю.')
        print('1 - Сказати людям правду')
        print('2 - Приховати інформацію')
        d = safe_input_int('> ', 1, 2)
        if d == 1:
            player['hope'] -= 10
            player['newspaper_trust'] += 10
            print('Люди знають правду.')
            print('Страх є, але довіра зросла.')
        if d == 2:
            player['discontent'] -= 5
            player['newspaper_trust'] -= 10
            print('Людей засокоїли.')
            print('Але якщо правда розкриється - буде ще гірше.')
    choice = player_action(player)
    if choice == '1':
        print('Куди відправляти робітників?')
        print('1 - Вугілля | 2 - Їжа | 3 - Дерево | 4 - Сталь')
        work = safe_input_int('> ', 1, 4)
        if work == 1:
            player['coal'] += 25
            player['discontent'] += 2
            print('Ми знайшли достатньо вугілля на день але люди втомлені і злі!\n')
        elif work == 2:
            player['food'] += 20
            print('Ми знайшли трохи їжі. (Їжа + 20)\n')
        elif work == 3:
            player['wood'] += 15
            print('Ми знайшли достатньо деревини поблизу.\n')
        elif work == 4:
            player['steel'] += 10
            print('Ми натрапили на залізну руду.\n')
    if choice == '2':
        if player['sick'] > 0 and player['food'] >= 5:
            player['sick'] -= 2
            player['food'] -= 5
            player['hope'] += 2
            print('Частину хворих вилікувано.\n')
        else:
            print('Немає ресурсів на лікування.\n')
    if choice == '3':
        print('Доступні закони:')
        for i in range(len(player['laws'])):
            if player['laws_state'][i] == 0:
                print (i + 1, '-', player['laws'][i])
        player['law_choice'] = safe_input_int('> ', 1, len(player['laws']))
        idx = player['law_choice'] - 1
        if idx >= 0 and idx < len(player['laws']) and player['laws_state'][idx] == 0:
            player['laws_state'][idx] = 1
            player['hope'] -= 3
            player['discontent'] += 3
            if idx == 0:
                player['coal'] += 15
                player['steel'] += 5
                player['factions_trust'][0] -= 10
                player['trust'] -= 5
            if idx == 1:
                player['wood'] += 20
                player['discontent'] += 5
                player['factions_trust'][0] -= 15
                player['factions_trust'][2] -= 10
                player['rumors'] += 5
            if idx == 2:
                player['food'] += 30
                player['hope'] -= 5
            if idx == 3:
                player['hope'] += 10
                player['factions_trust'][2] += 15
                player['trust'] += 5
            if idx == 4:
                player['discontent'] -= 5
    if choice == '4':
        print(f"Генератор: рівень {player['generator_level']}")
        print('1 - Підвищити рівень (вугілля - 20)')
        print('2 - Нічого не робити')
        g = safe_input_int('> ', 1, 2)
        if g == 1 and player['coal'] >= 20:
            player['generator_level'] += 1
            player['coal'] -= 20
            player['hope'] += 3
            player['temp'] += 10
            print('Генератор працює сильніше. Місту тепліше.')
        else:
            print('Недостатньо вугілля або скасовано.')
    if choice == '5':
        print('Що побудувати?')
        print('1 - Будинки (дерево - 15)')
        print('2 - Медпункт (дерево - 10, сталь - 5)')
        print('3 - Майстерня (дерево - 20, сталь - 10)')
        b = input('> ')
        if b == '1' and player['wood'] >= 15:
            player['houses'] += 1
            player['wood'] -= 15
            player['hope'] += 2
            print('Нові будинки збудовані.')
        elif b == '2' and player['wood'] >= 10 and player['steel'] >= 5:
            player['medical_post'] += 1
            player['wood'] -= 10
            player['steel'] -= 5
            player['sick'] -= 5
            print('Медпункт допомагає хворим.')
        elif b == '3' and player['wood'] >= 20 and player['steel'] >= 10:
            player['workshops'] += 1
            player['wood'] -= 20
            player['steel'] -= 10
            player['hope'] += 5
            print('Майстерня прискорює розвиток.')
    if choice == '6':
        if player['scouts_sent'] == 0 and player['people'] >= 5:
            player['scouts_sent'] = 1
            player['people'] -= 5
            print('Розвідники вирушили у білу пустку...')
        elif player['scouts_sent'] == 1:
            player['scouts_sent'] = 0
            player['food'] += 25
            player['coal'] += 20
            player['people'] += 5
            player['hope'] += 5
            print('Розвідники повернулись з ресурсами і людьми!')
    if choice == '7' and player['ideology'] == 0:
        print('⚖️ МІСТО НА РОЗДОРІЖЖІ')
        print('Оберіть шлях розвитку суспільства')
        print('1 - Порядок (сила, дисципліну, контроль)')
        print('2 - Віра (надія, духовність, єдність)')
        print('3 - Свобода (голос народу, вибір, довіра)')
        i = input('> ')
        if i == '1':
            player['ideology'] = 1
            player['ideology_name'] = 'Порядок'
            player['discontent'] -= 10
            player['hope'] -= 5
            print('Місто обрало порядок. Люди бояться, але слухаються.')
        elif i == '2':
            player['ideology'] = 2
            player['ideology_name'] = 'Віра'
            player['hope'] += 15
            print('Місто обрало віру. Люди моляться і тримаються разом.')
        elif i == '3':
            player['ideology'] = 3
            player['ideology_name'] = 'Свобода'
            player['discontent'] += 5
            player['hope'] += 5
            print('Місто обрало свободу. Люди мають голос.')
    if choice == '8':
        print('Що робити з газетою?')
        print('1 - Дозволити писати правду')
        print('2 - Контролювати інформацію')
        g = input('> ')
        if g == '1':
            player['hope'] += 3
            player['newspaper_trust'] += 5
            player['discontent'] += 1
            print('Газета пише правду. Люди довіряють але хвилюються.')
        if g == '2':
            player['discontent'] -= 3
            player['newspaper_trust'] -= 5
            print('Газету контролюють. Спокій є, але довіра падає.')
    if choice == '9':
        print('Ви нічого не зробили цього дня')
    if player['discontent'] > 80:
        player['people'] -= 5
        print('Люди залишають місто!')
    if player['sick'] > player['people']:
        player['sick'] = player['people']
    if player['temp'] < -40:
        player['sick'] += 3
        player['hope'] -= 5
    if player['discontent'] > 70 and player['ultimatum'] == -1:
        player['ultimatum'] = 3
        print('⚠️ УЛЬТИМАТУМ НАРОДУ ⚠️')
        print('Люди вимагають змін!')
        print('У вас є 3 дні, щоб знизити невдоволення або підняти надію.')
    if player['ultimatum'] > 0:
        player['ultimatum'] -= 1
        print(f"⏳ Днів до повстання: {player['ultimatum']}")
        if player['discontent'] <= 60 or player['hope'] >= 60:
            player['ultimatum'] = -1
            print('✅ Народ заспокоївся. Ультиматум знято.')
    if player['ultimatum'] == 0:
        print('❌ ПОВСТАННЯ!')
        print('Люди вигнали вас з міста...')
        player['people'] = 0
        break
    if player['day'] >= 26:
        if player['coal'] <= 0:
            player['hope'] -= 5
            player['people'] -= 2
            print('Без вугілля люди замерзають...')
        if player['temp'] < - 60:
            player['people'] -= 3
            print('Смертельний холод забирає життя.')
    if player['hope'] > 100:
        player['hope'] = 100
    if player['discontent'] < 0:
        player['discontent'] = 0
    if player['sick'] < 0:
        player['sick'] = 0
    if player['food'] < 0:
        player['food'] = 0
    if player['day'] % 6 == 0:
        print('👥 ГРОМАДЯНСЬКА ПОДІЯ')
        print('1 - Виступити з промовою')
        print('2 - Ігрнорувати людей')
        print('3 - Покарати оранізаторів')
        social = input('> ')
        if social == '1':
            player['trust'] += 5
            player['hope'] += 5
            print('Люди почули вас.')
        elif social == '2':
            player['trust'] -= 5
            player['rumors'] += 5
            print('Люди розчаровані мовчанням.')
        elif social == '3':
            player['trust'] -= 10
            player['discontent'] += 10
            print('Страх зростає, але порядок відновлено.')
    if player['rumors'] >= 20:
        print('🗣️ ЧУТКИ ПОШИРЮЮТЬСЯ!')
        player['hope'] -= 5
        player['trust'] -= 5
        player['rumors'] -= 10
    if player['trust'] <= 20 and player['leader_alive'] == 1:
        print('⚠️ Зʼявився лідер опозиції')
        print('1 - Переговори')
        print('2 - Усунути силою')
        l = input('> ')
        if l == '1':
            player['trust'] += 10
            player['hope'] += 5
            print('Компроміс досягнуто.')
        elif l == '2':
            player['leader_alive'] = 0
            player['trust'] -= 15
            player['discontent'] += 15
            print('Лідера усунено. Люди налякані.')
    if player['ideology'] == 1:
        player['discontent'] -= 1
        if player['discontent'] < 0:
            player['discontent'] = 0
    if player['ideology'] == 2:
        if player['sick'] > 0:
            player['sick'] -= 1
    if player['ideology'] == 3:
        player['hope'] += 1
    print('📊 Статистика міста')
    print(f'Дні: {player["day"] - 1}')
    print(f'Людей залишилось: {player["people"]}')
    print(f'Законів прийнято: {sum(player["laws_state"])}')
    print(f'Рівень генератора: {player["generator_level"]} \n\n')
    player['day'] += 1
    player['hope'] -= 1
    player['discontent'] += 1
hard_laws = 0
soft_laws = 0
if player['laws_state'][0] == 1:
    hard_laws += 1
if player['laws_state'][1] == 1:
    hard_laws += 1
if player['laws_state'][4] == 1:
    hard_laws += 1
if player['laws_state'][3] == 1:
    soft_laws += 1
def end_game(player):
    print('КІНЕЦЬ ГРИ')
    if player['people'] <= 0:
        print('❌ Місто загинуло.')
        print('Холод виявився сильнішим за людей.')
    elif player['hope'] <= 0:
        print('❌ Люди втратили віру.')
        print('Місто покинуте серед криги.')
    else:
        print('✅ Місто пережило холод.')
        if hard_laws >= 2 and player['discontent'] >= 60:
            print('🏆 СЕКРЕТНА КІНЦІВКА: ЗАЛІЗНИЙ КАПІТАН')
            print('Ви врятували місто будь-якою ціною.')
            print('Люди бояться вас, але вони живі.')
            print('Історія запамʼятає вас як тирана-рятівника.')
        elif soft_laws >= 1 and player['hope'] >= 70 and player['discontent'] <= 40:
            print('🏆 СЕКРЕТНА КІНЦІВКА: ЛЮДЯНИЙ КАПІТАН')
            print('Ви зберегли не лише життя, а й людяність.')
            print('Люди довіряють вам.')
            print('Місто вистояло разом із надією.')
        elif player['generator_level'] >= 3:
            print('🏆 СЕКРЕТНА КІНЦІВКА: ВОЛОДАР КРИГИ')
            print('Генератор став серцем нового світу.')
            print('Твоє місто - маяк для інших.')
            print('Це лише початок нової цивілізації.')
        elif player['trust'] >= 80 and player['hope'] >= 60:
            print('🏆 СЕКРЕТНА КІНЦІВКА: БАТЬКО МІСТА')
            print('Люди довіряють вам без страху.')
            print('Ви стали символом єдності.')
        else:
            print('🔷 ЗВИЧАЙНА КІНЦІВКА')
            print('Місто вижило.')
            print('Ви виконали свій обовʼязок Капітане')
end_game(player)