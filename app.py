import streamlit as st
from datetime import datetime
import pandas as pd

# Конфигурация страницы
st.set_page_config(
    page_title="Комплексный план лечения - Сплинт-терапия",
    page_icon="🦷",
    layout="wide"
)

# Инициализация состояния сессии
if 'diagnosis_data' not in st.session_state:
    st.session_state.diagnosis_data = {}
if 'treatment_data' not in st.session_state:
    st.session_state.treatment_data = {}
if 'goals_data' not in st.session_state:
    st.session_state.goals_data = {}

# Заголовок приложения
st.title("🦷 Комплексный план лечения - Сплинт-терапия")
st.markdown("---")

# Функция валидации ФИО
def validate_name(name):
    if not name.strip():
        return False, "Поле не может быть пустым"
    if ' ' not in name.strip():
        return False, "Вы не ввели инициалы!"
    parts = name.strip().split()
    if len(parts) < 2:
        return False, "Введите фамилию и инициалы"
    return True, ""

# СЕКЦИЯ 1: ШАПКА ДОКУМЕНТА
st.header("📋 Заполняем шапку")
st.info("Аккуратно и внимательно заполните все поля, выберите нужные чекбоксы и селекторы")

col1, col2 = st.columns([2, 1])

with col1:
    # Номер договора
    contract_number = st.text_input(
        "Номер договора:",
        #value="Абвгдежз-ИК/Лм-НОП-рст",
        help="Введите номер договора"
    )
    
    # Дата заключения
    contract_day = st.number_input(
        "Дата заключения договора (только две цифры):",
        min_value=1, max_value=31, value=datetime.now().day
    )
    
    # Месяц
    months = ["января", "февраля", "марта", "апреля", "мая", "июня",
              "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    contract_month = st.selectbox(
        "Месяц заключения договора:",
        months #,
        # value=datetime.now().month - 1  # текукщий по умолчанию
    )
    
    # Год
    contract_year = st.number_input(
        "Год заключения договора (только две цифры):",
        min_value=20, max_value=99, value=datetime.now().year % 100
    )
    
    # Пациент
    patient_name = st.text_input(
        "Про пациента — Фамилия, инициалы:",
        # value="Бакальчук Т.В.",
        help="Введите фамилию и инициалы через пробел"
    )
    
    # Валидация имени пациента
    if patient_name:
        is_valid, error_msg = validate_name(patient_name)
        if not is_valid:
            st.error(f"❌ {error_msg}")
    
    # Доктор
    doctor_name = st.text_input(
        "Про доктора — Фамилия, инициалы:",
        # value="Михайличенко В.Д.",
        help="Введите фамилию и инициалы через пробел"
    )
    
    # Валидация имени доктора
    if doctor_name:
        is_valid, error_msg = validate_name(doctor_name)
        if not is_valid:
            st.error(f"❌ {error_msg}")

# with col2:
#     st.info("""
#     **Можно и нужно заполнять:**
#     1. Желтые поля
#     2. Чекбоксы  
#     3. Селекторы
#     """)

st.markdown("---")

# СЕКЦИЯ 2: ДИАГНОЗЫ
st.header("🔍 Заполняем диагноз")

# Счетчики для проверки
main_diagnosis_count = 0
selected_diagnoses = []

# Диагнозы К07.6 — болезни ВЧНС
st.subheader("Диагнозы К07.6 — болезни ВЧНС")

col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.write("**Диагноз**")
with col2:
    st.write("**Основной**")
with col3:
    st.write("**Сопутствующий**")

# Список диагнозов К07.6
k07_diagnoses = [
    ("k07_60", "К07.60 — синдром болевой дисфункции ВНЧС"),
    ("k07_61", "К07.61 — «щёлкающая» челюсть"),
    ("k07_62", "К07.62 — рецидивирующий вывих и подвывих ВНЧС"),
    ("k07_63", "К07.63 — боль в ВНЧС не квалифицированная в других рубриках"),
    ("k07_64", "К07.64 — тугоподвижность ВНЧС не квалифицированная в других рубриках"),
    ("k07_65", "К07.65 — остеофит ВНЧС"),
    ("k07_68", "К07.68 — другие уточнённые болезни"),
    ("k07_69", "К07.69 — болезнь ВНЧС неуточненная")
]

for diag_id, diag_name in k07_diagnoses:
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(diag_name)
    with col2:
        main_selected = st.checkbox("", key=f"{diag_id}_main")
        if main_selected:
            main_diagnosis_count += 1
            selected_diagnoses.append(("main", diag_name))
    with col3:
        secondary_selected = st.checkbox("", key=f"{diag_id}_secondary")
        if secondary_selected:
            selected_diagnoses.append(("secondary", diag_name))

st.markdown("---")

# Артропатии, миалгия
st.subheader("Артропатии, миалгия")

arthropathy_diagnoses = [
    ("m05", "M05 — серопозитивный ревматоидный артрит"),
    ("m08", "M08 — юношеский (ювенальный) артрит"),
    ("m12_5", "M12.5Х — травматическая артропатия ВНЧС"),
    ("m19_0", "M19.0Х — первичный артроз ВНЧС"),
    ("m79_1", "M79.1 — миалгия")
]

for diag_id, diag_name in arthropathy_diagnoses:
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(diag_name)
    with col2:
        main_selected = st.checkbox("", key=f"{diag_id}_main")
        if main_selected:
            main_diagnosis_count += 1
            selected_diagnoses.append(("main", diag_name))
    with col3:
        secondary_selected = st.checkbox("", key=f"{diag_id}_secondary")
        if secondary_selected:
            selected_diagnoses.append(("secondary", diag_name))

st.markdown("---")

# Ручной ввод диагнозов
st.subheader("Ручной ввод")

manual_diagnoses = [
    ("ds01", "DS01 — Диагноз, прописанный вручную докторами №1"),
    ("ds02", "DS02 — Другой диагноз, прописанный вручную №2"),
    ("ds03", "DS03 — Диагноз, которого нет в справочнике и прописанный вручную №3")
]

for diag_id, diag_name in manual_diagnoses:
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(diag_name)
    with col2:
        main_selected = st.checkbox("", key=f"{diag_id}_main")
        if main_selected:
            main_diagnosis_count += 1
            selected_diagnoses.append(("main", diag_name))
    with col3:
        secondary_selected = st.checkbox("", key=f"{diag_id}_secondary")
        if secondary_selected:
            selected_diagnoses.append(("secondary", diag_name))

# Проверка основного диагноза
if main_diagnosis_count == 0:
    st.error("❌ Не выбран основной диагноз!")
elif main_diagnosis_count > 1:
    st.error("❌ Выбрано слишком много основных диагнозов! Должен быть только один.")
else:
    st.success("✅ Основной диагноз выбран корректно")

st.markdown("---")

# СЕКЦИЯ 3: ЛЕЧЕНИЕ
st.header("💊 Заполняем лечение")

st.subheader("Сплинт-терапия с помощью:")

# Типы сплинтов
splint_types = [
    ("miorel", "миорелаксирующего сплинта"),
    ("stabil", "стабилизирующего сплинта"),
    ("distr", "дистракционного сплинта"),
    ("anatom", "анатомического сплинта"),
    ("manual_type", "позиции, добавленной вручную")
]

selected_splints = []
for splint_id, splint_name in splint_types:
    selected = st.checkbox(splint_name, key=f"splint_{splint_id}")
    if selected:
        selected_splints.append(splint_name)

# Депрограмматор
deprogrammer = st.checkbox("депрограмматора длительного ношения", key="deprogrammer")

st.markdown("---")

# Цель лечения
st.subheader("Цель лечения (для ...):")

treatment_goals = [
    ("separate", "разобщения суставных поверхностей ВНЧС"),
    ("decompress", "декомпрессии ВНЧС"),
    ("correct_muscles", "коррекции работы мышц ЧЛО"),
    ("relax_muscles", "расслабления мышц ЧЛО"),
    ("position_jaw", "определения комфортной позиции нижней челюсти"),
    ("correct_condyles", "коррекции позиции мыщелков ВНЧС"),
    ("reposition_discs", "создания условий для репозиции дисков ВНЧС"),
    ("strengthen_apparatus", "создания условий для укрепления мышечно-связочного аппарата ВНЧС")
]

selected_goals = []
goal_count = 0
for goal_id, goal_name in treatment_goals:
    selected = st.checkbox(goal_name, key=f"goal_{goal_id}")
    if selected:
        selected_goals.append(goal_name)
        goal_count += 1

if goal_count == 0:
    st.error("❌ Не выбрана цель!")
else:
    st.success(f"✅ Выбрано целей: {goal_count}")

st.markdown("---")

# СЕКЦИЯ 4: ПРЕДВАРИТЕЛЬНЫЙ ПРОСМОТР
st.header("📄 Предварительный просмотр плана лечения")

if st.button("Сгенерировать план лечения", type="primary"):
    # Проверяем обязательные поля
    errors = []
    
    if not patient_name.strip():
        errors.append("Не указано имя пациента")
    elif not validate_name(patient_name)[0]:
        errors.append("Некорректное имя пациента")
    
    if not doctor_name.strip():
        errors.append("Не указано имя доктора")
    elif not validate_name(doctor_name)[0]:
        errors.append("Некорректное имя доктора")
        
    if main_diagnosis_count != 1:
        errors.append("Должен быть выбран ровно один основной диагноз")
        
    if not selected_splints and not deprogrammer:
        errors.append("Не выбран тип сплинта")
        
    if goal_count == 0:
        errors.append("Не выбрана цель лечения")
    
    if errors:
        st.error("Невозможно сгенерировать план. Ошибки:")
        for error in errors:
            st.write(f"• {error}")
    else:
        # Генерируем план лечения
        st.success("✅ План лечения сгенерирован успешно!")
        
        # Отображаем итоговый документ
        with st.expander("📋 Готовый план лечения для печати", expanded=True):
            
            # Шапка документа
            st.markdown(f"""
            **Приложение к договору о предоставлении медицинских услуг № {contract_number}**  
            от «{contract_day}» {contract_month} 20{contract_year} г.
            
            ### План лечения
            
            **Дата:** {datetime.now().strftime("%d.%m.%Y")}  
            **Пациент:** {patient_name}
            """)
            
            # Диагнозы
            main_diag = [diag[1] for diag in selected_diagnoses if diag[0] == "main"]
            secondary_diag = [diag[1] for diag in selected_diagnoses if diag[0] == "secondary"]
            
            if main_diag:
                st.markdown(f"**Диагноз:** {main_diag[0]}")
            
            if secondary_diag:
                st.markdown(f"**Сопутствующий диагноз:** {'; '.join(secondary_diag)}")
            
            # Лечение
            treatment_text = "сплинт-терапия с помощью "
            if selected_splints:
                treatment_text += ", ".join(selected_splints)
            if deprogrammer:
                if selected_splints:
                    treatment_text += ", с депрограмматором длительного ношения"
                else:
                    treatment_text += "депрограмматора длительного ношения"
            
            st.markdown(f"**Лечение:** {treatment_text}")
            
            if selected_goals:
                goals_text = "; ".join(selected_goals)
                st.markdown(f"**для** {goals_text}.")
            
            # Стандартные рекомендации
            st.markdown("""
            **Режим использования:**  
            рекомендовано использование аппарата во время обострений и при выполнении миогимнастики.
            
            На этапе сплинт-терапии возможна коррекция высоты и окклюзионной поверхности аппарата путем перебазировки. В этом случае аппарат будет необходимо передать на некоторое время в зуботехническую лабораторию.
            
            После 3 месяцев использования окклюзионного аппарата — контроль состояния мышц челюстно-лицевой области и височно-нижнечелюстного сустава (МРТ ВНЧС). В случае отсутствия положительной динамики или появления других симптомов дисфункции ВНЧС и мышц ЧЛО может быть предложена консультация смежных специалистов (остеопата, невролога, челюстно-лицевого хирурга, психиатра). Кроме этого, план лечения может быть скорректирован.
            
            При усилении симптомов гипертонуса мышц челюстно-лицевой области может быть использована аппаратная депрограммация мышц в клинике, коррекция комплекса миогимнастики, терапевтическое тейпирование, а также консультация смежных специалистов.
            
            **По окончании сплинт терапии может быть рекомендовано:**  
            повторная диагностика (КЛКТ, МРТ ВНЧС, аксиография, миография, цифровое моделирование окклюзионной поверхности зубов); постепенный отказ от использования аппарата с клиническим наблюдением (сплинт-каникулы) и последующей коррекцией плана лечения.
            
            В случае утери аппарата необходимо изготовить новый, оплатив его полную стоимость. В случае поломки аппарата проводится его ремонт (если это возможно). Гарантийный срок службы для окклюзионных аппаратов (сплинтов) не предусмотрен.
            """)
            
            # Подписи
            st.markdown(f"""
            ---
            **Пациент:** _________________ / {patient_name} /  
            **Врач:** _________________ / {doctor_name} /  
            """)

# Подвал
st.markdown("---")
st.caption("© ОФС Стоматология, https://ofs.team/")
st.caption("Система комплексного планирования лечения • Версия 1.0")
