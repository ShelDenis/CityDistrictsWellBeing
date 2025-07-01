import streamlit as st
import pickle
from top import colors


green_values = ['Зелени очень мало',
                'Зелени не очень много, где-то посажены деревья',
                'В микрорайоне есть сквер/парк']
water_values = ['Рядом нет водных объектов',
                'Рядом есть озеро/пруд',
                'Микрорайон имеет набережную реки']
jd_values = ['Рядом нет железной дороги',
             'Рядом лежит железная дорога',
             'Микрорайон располагается рядом с ЖД вокзалом']
school_values = ['Школы нет даже в соседних микрорайонах',
                 'Школа есть только в соседнем микрорайоне',
                 'В микрорайоне есть одна-две школы']
kgarten_values = ['Детского сада нет даже в соседних микрорайонах',
                  'Детский сад есть только в соседнем микрорайоне',
                  'В микрорайоне есть один-два детских сада']
supemarket_values = ['В микрорайоне ни одного сетевого супермаркета, в лучшем случае - есть магазин ИП',
                     'В микрорайоне есть 1-2 сетевых супермаркета',
                     'В микрорайоне есть все или почти все возможные сетевые супермакеты']
mall_values = ['В ближайших микрорайонах нет ТЦ',
               'ТЦ есть в ближайшем микрорайоне',
               'В микрорайоне есть крупный ТЦ']
transport_values = ['В лучшем случае из микрорайона можно выехать на автобусе одного маршрута',
                    'Микрорайон соединяют 4-5 автобусных маршрутов с разными частями города',
                    'Из микрорайона можно уехать на общественном транспорте в любой другой район города']
type_values = ['деревянный частный сектор',
               'многоэтажные дома',
               'коттеджный поселок']

marks = {
    9: 'Высокий уровень благополучия',
    8: 'Высокий уровень благополучия',
    7: 'Средний уровень благополучия',
    6: 'Средний уровень благополучия',
    5: 'Низкий уровень благополучия',
    4: 'Низкий уровень благополучия',
    3: 'Далеко не благополучный район',
    2: 'Далеко не благополучный район',
    1: 'Далеко не благополучный район',
}


def prediction():
    st.header('Предсказание благополучия микрорайона')
    st.text('По объективным признакам с помощью ИИ можно приблизительно узнать уровень'
            ' благополучия микрорайона. Для этого нужно ввести данные, которые можно'
            ' взять с онлайн-карт.')

    st.image('data/cristall.jpg')

    dist = st.slider("Расстояние до цента города (км):", 0, 50, 5)

    green = st.selectbox('Насколько "зеленый" микрорайон?', green_values)
    water = st.selectbox('Как в микрорайоне обстоит дело с водными объектами?', water_values)
    station = st.selectbox('Есть ли рядом с микрорайоном железная дорога?', jd_values)
    bridge = st.selectbox('Отделен ли микрорайон от центра города мостом (виадуком/эстакадой)?', ['да', 'нет'])
    factory = st.selectbox('Расположены ли рядом с микрорайоном заводы?', ['да', 'нет'])

    floors = st.slider("Максимальное количество этажей в домах микрорайона:", 1, 50, 5)

    school = st.selectbox('Оцените обеспеченность микрорайона школами:', school_values)
    kgarten = st.selectbox('Оцените обеспеченность микрорайона детскими садами:', kgarten_values)
    supermarket = st.selectbox('Достаточно ли в микрорайоне супермаркетов?', supemarket_values)
    mall = st.selectbox('Есть ли в микрорайоне крупные торговые центры?', mall_values)
    transport = st.selectbox('Хорошо ли микрорайон обеспечен общественным транспортом?', transport_values)
    gas_station = st.selectbox('Расположены ли рядом с микрорайоном АЗС?', ['да', 'нет'])
    type = st.selectbox('Укажите тип микрорайона', type_values)

    if st.button('Узнать результат!'):
        lists = [green_values, water_values, jd_values, school_values, kgarten_values,
                 supemarket_values, mall_values, transport_values, type_values]
        values = [green, water, station, school, kgarten,
                  supermarket, mall, transport, type]

        for i in range(len(lists)):
            values[i] = lists[i].index(values[i])

        yes_no_vals = [bridge, factory, gas_station]

        for i in range(len(yes_no_vals)):
            if yes_no_vals[i] == 'да':
                yes_no_vals[i] = 1
            else:
                yes_no_vals[i] = 0

        list_to_predict = ([dist] + values[:3] + yes_no_vals[:2] +
                           [floors] + values[3:-1] + [yes_no_vals[-1]] + [values[-1]])

        models = ['linear', 'lasso', 'ridge', 'bagging', 'boosting', 'stacking']
        for m in models:
            with open(f'models/{m}.pkl', 'rb') as file:
                model = pickle.load(file)
                pred = model.predict([list_to_predict])[0]

                st.markdown(
                    f"""
                    Модель {m.capitalize()}
                            <div style="background-color: #{colors[pred // 10]}; padding: 10px; border-radius: 5px;">
                                <p>{marks[pred // 10]} (<b>{round(pred, 2)}%</b>)
                            </div>
                            """,
                    unsafe_allow_html=True
                )