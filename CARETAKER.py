from tkinter import *
from tkinter import messagebox, Tk , Label
import numpy as np
import pandas as pd



l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

disease=['Fungal infection  \n Precaution to be taken: Wear clean and dry clothes, Avoid wearing tight clothes and shoes, Bathe at least once a day, Keep your nails short and clean, Add probiotics (foods with live bacteria beneficial to your health) to your diet as the bacteria can help your body fight against the harmful fungi that cause infections. ',
         'Allergy  \n Precaution to be taken: Avoid all the allergens completely to which you are sensitive, Take allergy shots for seasonal allergies caused by pollen, Keep a diary to tack what to eat and what not to eat, Consult a specialist for the treatment of a particular allergy',
         'GERD  \n Nonprescription medication: Medications to reduce acid production, Medications that block acid production and heal the esophagus',
         'Chronic cholestasis  \n Precaution to be taken: Get vaccinated for hepatitis, Do not abuse alcohol, Avoid using recreational intravenous drugs',
         'Drug Reaction  \n Precaution to be taken: Know why you are taking each medication, Know how to take the drug, Go easy on grapefruit juice, Talk to your pharmacist',
        'Peptic ulcer diseae  \n Precaution to be taken: Washing your hands frequently to avoid infections, Limiting your use of ibuprofen, aspirin, and naproxen (Aleve), Not drinking more than two alcoholic beverages a day',
        'AIDS  \n Precaution to be taken: Protect yourself during during sex, Protect Yourself during drugs, Protect others if you have HIV.',
        'Diabetes  \n Precaution to be taken: Lose extra weight, Be more physically active, Eat healthy plant foods, Skip fad diets and make healthier choices.',
        'Gastroenteritis  \n Precaution to be taken: Always wash your hands, especially before eating or while preparing food, Vaccination available against certain types of bacteria and virus needs to be taken,Do not drink too much fluid at once, Do not share your personal items such as tooth brush, spoons, or towels',
        'Bronchial Asthma  \n Precaution to be taken: Identify and avoid the triggers - triggers could be exercise, certain foods, pollen. \n Monitor your breathing often. If you suspect breathing difficulty, wheezing or cough, it is recommended to see the doctor.',
        'Hypertension  \n Precaution to be taken: Maintain a healthy weight, Get regular exercise, Learn to manage tension or stress, Take a well-balanced diet rich in calcium, potassium, and magnesium',
        'Migraine  \n Precaution to be taken: Practise the right sleep-wake cycle, Eat your meals at the right time, Avoid strenuous activities, including intense exercises, Learn to manage stress',
        'Cervical spondylosis  \n Medication: Anti-inflammatory drugs: Reduce swelling and pain, Muscle relaxants: Treat muscle spasms, Anticonvulsants: Reduce pain from damaged nerves. Usually given if symptoms are severe.',
        'Paralysis (brain hemorrhage)  \n Precaution to be taken: Removing tripping hazards from your home – especially if you are elderly, Having your vision checked regularly to prevent falls and accidents, Having your healthcare provider or pharmacist do a medication review.',
        'Jaundice  \n Precaution to be taken: Eat Fresh Food, consume clean water, frequent hydration, avoid alcohol consumption, maintain wait , maintain hygiene.',
        'Malaria  \n Precaution to be taken: Sleep under nets, to prevent mosquito bites, Try to minimise body exposure by wearing long pants and long sleeved shirts, Mosquito repellent creams or sprays are available.',
        'Chicken pox  \n Precaution to be taken: The best way to prevent chickenpox is to get the chickenpox vaccine, Chickenpox vaccine is very safe and effective at preventing the disease.',
        'Dengue  \n Precaution to be taken: Maintain a clean and mosquito-free environment, Take dengue patients to the hospital daily, Ensure the patient gets sufficient bed rest, Give the patient Acetaminophen/paracetamol.',
        'Typhoid  \n Precaution to be taken: Avoid street food, Drink filtered water only, Maintain hygiene, if surrounded by the typhoid carrier, Increase the intake of fluid, Always wash your hands, Get vaccination if planning to visit typhoid prone area',
        'hepatitis A  \n Precaution to be taken: Wash your hands regularly, Take adequate rest, Eat high calorie foods, Quit alcohol.',
        'Hepatitis B  \n Precaution to be taken:Avoid multiple sex partners, Talk to your partner and get tested for HBV, Avoid sharing needles and syringes, Avoid body piercing and tattooing.',
        'Hepatitis C  \n Precaution to be taken: Never share needles or other injection equipment. If you use IV drugs, ask your doctor about substance abuse treatment programs, Always use bandages to cover up cuts and scratches.',
        'Hepatitis D  \n Precaution to be taken:Avoid sharing drug equipment, such as: needles spoons filters cookers pipes straws.',
        'Hepatitis E  \n Precaution to be taken: maintaining quality standards for public water supplies,  establishing proper disposal systems for human faeces.',
        'Alcoholic hepatitis  \n Precaution to be taken: Practise moderate alcohol intake, or quit drinking alcohol.',
        'Tuberculosis  \n Precaution to be taken: Covering one’s nose and mouth while sneezing or coughing can prevent the spread of TB infection, Isolation from college, schools and workplaces and crowded areas, Avoid sharing rooms and beds with other un-infected persons.',
        'Common Cold  \n Precaution to be taken: Wash hands with soap and water ,Disinfect kitchen, bathrooms, Sneeze into tissues and discard them, Avoid sharing of items such as utensils',
        'Pneumonia  \n Precaution to be taken: washing hands before eating, after touching people, and after going out in public, disinfecting all surfaces in the home, particularly if someone has recently been sick, keeping up-to-date on all vaccinations, especially any household members around infants who are too young to be vaccinated',
        'Dimorphic hemmorhoids(piles)  \n Precaution to be taken: Do not sit for a more extended period. Use a cushion while sitting on the chair, Do not avoid pooping. If you have the urge to do so, please go ahead, Do not strain while pooping. Avoid consuming a lot of time in the loo, Do not lift heavy objects',
        'Heartattack  \n Precaution to be taken: Stop smoking and minimize your exposure to secondhand smoke, Get your high blood cholesterol and high blood pressure under control by modifying your diet, losing weight, taking medication, or doing a combination of these things',
        'Varicoseveins  \n Precaution to be taken: Avoid prolonged periods of sitting or standing, Wear compression hosiery,Exercise should be part of your routine. ',
        'Hypothyroidism  \n Precaution to be taken: Avoid smoking or drinking alcohol, Say no to macronutrients,  Stay away from sugar and caffeine, No self-medication.',
        'Hyperthyroidism  \n Precaution to be taken: Check thyroid regularly, Drink a lot of water, Avoid smoking or drinking alcohol,  Stay away from sugar and caffeine.',
        'Hypoglycemia  \n Precaution to be taken: Identifying the symptoms and taking immediate action is the primary preventive measure, Let your family and friends know the symptoms of hypoglycaemia so as to get timely help, Discuss and check with your doctor if the medication doses can be altered, Read the instruction of your medications properly to keep yourself updated on their side effects',
        'Osteoarthristis  \n Medication: Analgesics- Drugs that are used to relieve pain, Nonsteroidal anti-inflammatory drugs (NSAIDs): Reduces pain and inflammation.',
        'Arthritis  \n Precaution to be taken: Maintain a healthy weight, protect your joints from injuries, Exercise is beneficial for your overall health as well as for your joints.',
        '(vertigo) Paroymsal  Positional Vertigo  \n Precaution to be taken: Be aware of the possibility of losing your balance, which can lead to falling and serious injury, Avoid movements, such as looking up, that bring on the symptoms, Sit down immediately when you feel dizzy, Use good lighting if you get up at nigh',
        'Acne  \n Precaution to be taken: Wash face twice daily, Avoid contact with greasy and oily substances, Protect skin from sun by applying moisturizers and sunscreens, Avoid friction and pressure on the skin',
        'Urinary tract infection  \n Precaution to be taken: Complete the prescribed course of antibiotics, Drink plenty of water to flush out the germs, Use heating pads to get relief from back pain',
        'Psoriasis  \n Precaution to be taken: Wrap up during cold, dry weather, Keep the skin moisturized, Keep the scalp moisturized, Get regular exposure to sunlight.',
        'Impetigo  \n Precaution to be taken: Avoid direct skin-to-skin contact with others, Resist the urge to touch (and scratch) your sores, Skip sharing personal items with others.']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)

def message():
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        NaiveBayes()

def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb=gnb.fit(X,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")

root = Tk()
root.title("CARETAKER")
root.configure()



# Adjust size 
# root.geometry("1600x1200")
  
# # Add image file
# bg = PhotoImage( file = "R (1).png")
  
# # Show image using label
# label1 = Label( root, image = bg)
# label1.place(x = 0,y = 0)

class Window(Frame):
    def __init__(self, master=None, bg = "#ADD8E6"):
        Frame.__init__(self, master)
        self.master = master
        self.master.configure(background='#ADD8E6')
root.geometry("400x300")
app = Window(root)


Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)

w2 = Label(root, justify=LEFT, text=" CARETAKER ")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb1 = Label(root, text="")
NameLb1.config(font=("Elephant", 20))
NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

S1Lb = Label(root,  text="Symptom 1")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

S2Lb = Label(root,  text="Symptom 2")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root,  text="Symptom 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root,  text="Symptom 4")
S4Lb.config(font=("Elephant", 15))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root,  text="Symptom 5")
S5Lb.config(font=("Elephant", 15))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)

lr = Button(root, text="Predict",height=2, width=20, command=message)
lr.config(font=("Elephant", 15))
lr.grid(row=15, column=1,pady=20)

OPTIONS = sorted(l1)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=2)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=2)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=2)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=2)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=2)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 20))
NameLb.grid(row=13, column=1, pady=10,  sticky=W)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 15))
NameLb.grid(row=18, column=1, pady=10,  sticky=W)

t3 = Text(root, height=5, width=80)
t3.config(font=("Elephant", 20))
t3.grid(row=20, column=1 , padx=10)

root.mainloop()
