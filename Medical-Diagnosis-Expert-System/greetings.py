from experta import *

class Greetings(KnowledgeEngine):

    def __init__(self, symptom_map, if_not_matched, get_details):
        self.symptom_map = symptom_map
        self.if_not_matched = if_not_matched
        self.get_details = get_details
        KnowledgeEngine.__init__(self)

    #code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        print("")
        print("This is a knowledge based bot to diagnose diseases")
        print("")
        print("Do you feel any of the following symptoms?")
        print("Reply high or low or no")
        print("")
        yield Fact(action="find_disease")

    #taking various input from user
    @Rule(Fact(action="find_disease"), NOT(Fact(headache=W())), salience=4)
    def symptom_0(self):
        self.declare(Fact(headache=input("headache: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(chills=W())), salience=1)
    def symptom_1(self):
        self.declare(Fact(chills=input("chills: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(chest_pain=W())), salience=1)
    def symptom_2(self):
        self.declare(Fact(chest_pain=input("chest pain: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(cough=W())), salience=3)
    def symptom_3(self):
        self.declare(Fact(cough=input("cough: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(fainting=W())), salience=1)
    def symptom_4(self):
        self.declare(Fact(fainting=input("fainting: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(fatigue=W())), salience=1)
    def symptom_5(self):
        self.declare(Fact(fatigue=input("fatigue: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(sunken_eyes=W())), salience=1)
    def symptom_6(self):
        self.declare(Fact(sunken_eyes=input("sunken eyes: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(vomiting=W())), salience=1)
    def symptom_7(self):
        self.declare(Fact(vomiting=input("vomiting: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(restlessness=W())), salience=1)
    def symptom_8(self):
        self.declare(Fact(restlessness=input("restlessness: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(sore_throat=W())), salience=1)
    def symptom_9(self):
        self.declare(Fact(sore_throat=input("sore throat: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(fever=W())), salience=1)
    def symptom_10(self):
        self.declare(Fact(fever=input("fever: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(nausea=W())), salience=1)
    def symptom_11(self):
        self.declare(Fact(nausea=input("nausea: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(blurred_vision=W())), salience=1)
    def symptom_12(self):
        self.declare(Fact(blurred_vision=input("blurred_vision: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(nasal_congestion=W())), salience=1)
    def symptom_13(self):
        self.declare(Fact(nasal_congestion=input("blurred vision: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(diarrhea=W())), salience=1)
    def symptom_14(self):
        self.declare(Fact(diarrhea=input("diarrhea: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(abdominal_pain=W())), salience=1)
    def symptom_15(self):
        self.declare(Fact(abdominal_pain=input("abdominal pain: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(muscular_pain=W())), salience=1)
    def symptom_16(self):
        self.declare(Fact(muscular_pain=input("muscular pain: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(low_sense_of_taste=W())), salience=1)
    def symptom_17(self):
        self.declare(Fact(low_sense_of_taste=input("low sense of taste: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(low_sense_of_smell=W())), salience=1)
    def symptom_18(self):
        self.declare(Fact(low_sense_of_smell=input("low sense of smell: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(breathing_difficulties=W())), salience=1)
    def symptom_19(self):
        self.declare(Fact(breathing_difficulties=input("breathing difficulties: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(accelerated_heartbeat=W())), salience=1)
    def symptom_20(self):
        self.declare(Fact(accelerated_heartbeat=input("accelerated heartbeat: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(swelling_eye=W())), salience=1)
    def symptom_21(self):
        self.declare(Fact(swelling_eye=input("swelling eye: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(itchy_eye=W())), salience=1)
    def symptom_22(self):
        self.declare(Fact(itchy_eye=input("itchy eye: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(burning_eye=W())), salience=1)
    def symptom_23(self):
        self.declare(Fact(burning_eye=input("burning eye: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(tearing_eye=W())), salience=1)
    def symptom_24(self):
        self.declare(Fact(tearing_eye=input("tearing eye: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(redness_eye=W())), salience=1)
    def symptom_25(self):
        self.declare(Fact(redness_eye=input("redness eye: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(involuntary_weight_loss=W())), salience=1)
    def symptom_26(self):
        self.declare(Fact(involuntary_weight_loss=input("involuntary weight loss: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(irritability=W())), salience=1)
    def symptom_27(self):
        self.declare(Fact(irritability=input("irritability: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(weakness=W())), salience=1)
    def symptom_28(self):
        self.declare(Fact(weakness=input("weakness: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(hand_numbness=W())), salience=1)
    def symptom_29(self):
        self.declare(Fact(hand_numbness=input("hand numbness: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(sleep_problems=W())), salience=1)
    def symptom_30(self):
        self.declare(Fact(sleep_problems=input("sleep problems: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(poor_apetite=W())), salience=1)
    def symptom_31(self):
        self.declare(Fact(poor_apetite=input("poor apetite: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(burning_sensation=W())), salience=1)
    def symptom_32(self):
        self.declare(Fact(burning_sensation=input("burning sensation: ")))
    
    @Rule(Fact(action="find_disease"), NOT(Fact(sensitivity_to_light=W())), salience=1)
    def symptom_33(self):
        self.declare(Fact(sensitivity_to_light=input("sensitivity to light: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(sound_sensitivity=W())), salience=1)
    def symptom_34(self):
        self.declare(Fact(sound_sensitivity=input("sound sensitivity: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(hyperactivity=W())), salience=1)
    def symptom_35(self):
        self.declare(Fact(hyperactivity=input("hyperactivity: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(neck_stifness=W())), salience=1)
    def symptom_36(self):
        self.declare(Fact(neck_stifness=input("neck stifness: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(facial_pressure=W())), salience=1)
    def symptom_37(self):
        self.declare(Fact(facial_pressure=input("facial pressure: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(stomach_cramps=W())), salience=1)
    def symptom_38(self):
        self.declare(Fact(stomach_cramps=input("stomach cramps: ")))
        
    @Rule(Fact(action="find_disease"), NOT(Fact(blood_in_stool=W())), salience=1)
    def symptom_39(self):
        self.declare(Fact(blood_in_stool=input("blood in stool: ")))
        
    # different rules checking for each disease match
    
    # Disease 0 - Accute Apendicitis
    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="high"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion=""),
        Fact(diarrhea="no"),
        Fact(abdominal_pain="high"),
        Fact(muscular_pain="no"),
        Fact(low_sense_of_taste="no"),
        Fact(low_sense_of_smell="no"),
        Fact(breathing_difficulties="no"),
        Fact(accelerated_heartbeat="no"),
        Fact(swelling_eye="no"),
        Fact(itchy_eye="no"),
        Fact(burning_eye="no"),
        Fact(tearing_eye="no"),
        Fact(redness_eye="no"),
        Fact(involuntary_weight_loss=""),
        Fact(irritability="no"),
        Fact(weakness="high"),
        Fact(hand_numbness="no"),
        Fact(sleep_problems="no"),
        Fact(poor_apetite="no"),
        Fact(burning_sensation="no"),
        Fact(sensitivity_to_light="no"),
        Fact(sound_sensitivity="no"),
        Fact(hyperactivity="no"),
        Fact(neck_stifness="no"),
        Fact(facial_pressure="no"),
        Fact(stomach_cramps="no"),
        Fact(blood_in_stool="no"),
    )
    def disease_0(self):
        self.declare(Fact(disease="Accute-apendicitis"))
        
    # Disease 1 - Asthma

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="no"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion="no"),
        Fact(diarrhea="no"),
        Fact(abdominal_pain="no"),
        Fact(muscular_pain="no"),
        Fact(low_sense_of_taste="no"),
        Fact(low_sense_of_smell="no"),
        Fact(breathing_difficulties="high"),
        Fact(accelerated_heartbeat="no"),
        Fact(swelling_eye="no"),
        Fact(itchy_eye="no"),
        Fact(burning_eye="no"),
        Fact(tearing_eye="no"),
        Fact(redness_eye="no"),
        Fact(involuntary_weight_loss="no"),
        Fact(irritability="no"),
        Fact(weakness="no"),
        Fact(hand_numbness="no"),
        Fact(sleep_problems="no"),
        Fact(poor_apetite="no"),
        Fact(burning_sensation="no"),
        Fact(sensitivity_to_light="no"),
        Fact(sound_sensitivity="no"),
        Fact(hyperactivity="no"),
        Fact(neck_stifness="no"),
        Fact(facial_pressure="no"),
        Fact(stomach_cramps="no"),
        Fact(blood_in_stool="no"),
    )
    def disease_1(self):
        self.declare(Fact(disease="Asthma"))
        
    # Disease 2 - Cardiac arrhythmia

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(fatigue="high"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="high"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion="no"),
        Fact(diarrhea="no"),
        Fact(abdominal_pain="no"),
        Fact(muscular_pain="no"),
        Fact(low_sense_of_taste="no"),
        Fact(low_sense_of_smell="no"),
        Fact(breathing_difficulties="no"),
        Fact(accelerated_heartbeat="high"),
        Fact(swelling_eye="no"),
        Fact(itchy_eye="no"),
        Fact(burning_eye="no"),
        Fact(tearing_eye="no"),
        Fact(redness_eye="no"),
        Fact(involuntary_weight_loss="no"),
        Fact(irritability="no"),
        Fact(weakness="no"),
        Fact(hand_numbness="no"),
        Fact(sleep_problems="no"),
        Fact(poor_apetite="no"),
        Fact(burning_sensation="no"),
        Fact(sensitivity_to_light="no"),
        Fact(sound_sensitivity="no"),
        Fact(hyperactivity="no"),
        Fact(neck_stifness="no"),
        Fact(facial_pressure="no"),
        Fact(stomach_cramps="no"),
        Fact(blood_in_stool="no"),
    )
    def disease_2(self):
        self.declare(Fact(disease="Cardiac-arrhythmia"))
        
    # Disease 3 - Conjunctivitis

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion=""),
        Fact(diarrhea=""),
        Fact(abdominal_pain=""),
        Fact(muscular_pain=""),
        Fact(low_sense_of_taste=""),
        Fact(low_sense_of_smell=""),
        Fact(breathing_difficulties="no"),
        Fact(accelerated_heartbeat="no"),
        Fact(swelling_eye="high"),
        Fact(itchy_eye="high"),
        Fact(burning_eye="high"),
        Fact(tearing_eye="high"),
        Fact(redness_eye="high"),
        Fact(involuntary_weight_loss="no"),
        Fact(irritability="no"),
        Fact(weakness="no"),
        Fact(hand_numbness="no"),
        Fact(sleep_problems="no"),
        Fact(poor_apetite="no"),
        Fact(burning_sensation="no"),
        Fact(sensitivity_to_light="no"),
        Fact(sound_sensitivity="no"),
        Fact(hyperactivity="no"),
        Fact(neck_stifness="no"),
        Fact(facial_pressure="no"),
        Fact(stomach_cramps="no"),
        Fact(blood_in_stool="no"),
    )
    def disease_3(self):
        self.declare(Fact(disease="Conjunctivitis"))
        
    # Disease 4 - Coronavirus

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(fatigue="high"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="high"),
        Fact(nasal_congestion="no"),
        Fact(diarrhea="no"),
        Fact(abdominal_pain="no"),
        Fact(muscular_pain="no"),
        Fact(low_sense_of_taste="no"),
        Fact(low_sense_of_smell="no"),
        Fact(breathing_difficulties="no"),
        Fact(accelerated_heartbeat="no"),
        Fact(general_pain="no"),
        Fact(swelling_eye="no"),
        Fact(itchy_eye="no"),
        Fact(burning_eye="no"),
        Fact(tearing_eye="no"),
        Fact(redness_eye="no"),
        Fact(involuntary_weight_loss="high"),
        Fact(irritability="high"),
        Fact(weakness="high"),
        Fact(hand_numbness="no"),
        Fact(sleep_problems="no"),
        Fact(poor_apetite="no"),
        Fact(burning_sensation="no"),
        Fact(sensitivity_to_light=""),
        Fact(sound_sensitivity=""),
        Fact(hyperactivity=""),
        Fact(neck_stifness=""),
        Fact(facial_pressure=""),
        Fact(stomach_cramps=""),
        Fact(blood_in_stool=""),
    )
    def disease_4(self):
        self.declare(Fact(disease="Coronavirus"))
        
    # Disease 5 - Diabetes
    
    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion=""),
        Fact(diarrhea=""),
        Fact(abdominal_pain=""),
        Fact(muscular_pain=""),
        Fact(low_sense_of_taste=""),
        Fact(low_sense_of_smell=""),
        Fact(breathing_difficulties=""),
        Fact(accelerated_heartbeat=""),
        Fact(general_pain=""),
        Fact(swelling_eye=""),
        Fact(itchy_eye=""),
        Fact(burning_eye=""),
        Fact(tearing_eye=""),
        Fact(redness_eye=""),
        Fact(involuntary_weight_loss=""),
        Fact(irritability=""),
        Fact(weakness=""),
        Fact(hand_numbness=""),
        Fact(sleep_problems=""),
        Fact(poor_apetite=""),
        Fact(burning_sensation=""),
        Fact(shudder=""),
        Fact(sensitivity_to_light=""),
        Fact(sound_sensitivity=""),
        Fact(hyperactivity=""),
        Fact(neck_stifness=""),
        Fact(facial_pressure=""),
        Fact(stomach_cramps=""),
        Fact(blood_in_stool=""),
    )
    def disease_5(self):
        self.declare(Fact(disease="Diabetes"))
        
    # Disease 6 - Fibromyalgia

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="high"),
        Fact(chills="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(fatigue="high"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="no"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion="no"),
        Fact(diarrhea="no"),
        Fact(abdominal_pain="no"),
        Fact(muscular_pain="no"),
        Fact(low_sense_of_taste="no"),
        Fact(low_sense_of_smell="no"),
        Fact(breathing_difficulties="no"),
        Fact(accelerated_heartbeat="no"),
        Fact(general_pain="high"),
        Fact(swelling_eye="no"),
        Fact(itchy_eye="no"),
        Fact(burning_eye="no"),
        Fact(tearing_eye="no"),
        Fact(redness_eye="no"),
        Fact(involuntary_weight_loss="no"),
        Fact(irritability="no"),
        Fact(weakness="high"),
        Fact(hand_numbness="high"),
        Fact(sleep_problems="high"),
        Fact(poor_apetite="no"),
        Fact(burning_sensation="no"),
        Fact(sensitivity_to_light="no"),
        Fact(sound_sensitivity="no"),
        Fact(hyperactivity="no"),
        Fact(neck_stifness="no"),
        Fact(facial_pressure="no"),
        Fact(stomach_cramps="no"),
        Fact(blood_in_stool="no"),
    )
    def disease_6(self):
        self.declare(Fact(disease="Fibromyalgia"))
        
    # Disease 7 - Gastritis falta

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion=""),
        Fact(diarrhea=""),
        Fact(abdominal_pain=""),
        Fact(muscular_pain=""),
        Fact(low_sense_of_taste=""),
        Fact(low_sense_of_smell=""),
        Fact(breathing_difficulties=""),
        Fact(accelerated_heartbeat=""),
        Fact(general_pain=""),
        Fact(swelling_eye=""),
        Fact(itchy_eye=""),
        Fact(burning_eye=""),
        Fact(tearing_eye=""),
        Fact(redness_eye=""),
        Fact(involuntary_weight_loss=""),
        Fact(irritability=""),
        Fact(weakness=""),
        Fact(hand_numbness=""),
        Fact(sleep_problems=""),
        Fact(poor_apetite=""),
        Fact(burning_sensation=""),
        Fact(shudder=""),
        Fact(sensitivity_to_light=""),
        Fact(sound_sensitivity=""),
        Fact(hyperactivity=""),
        Fact(neck_stifness=""),
        Fact(facial_pressure=""),
        Fact(stomach_cramps=""),
        Fact(blood_in_stool=""),
    )
    def disease_7(self):
        self.declare(Fact(disease="Gastritis"))
        
    # Disease 8 - Hiatal hernia 

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion=""),
        Fact(diarrhea=""),
        Fact(abdominal_pain=""),
        Fact(muscular_pain=""),
        Fact(low_sense_of_taste=""),
        Fact(low_sense_of_smell=""),
        Fact(breathing_difficulties=""),
        Fact(accelerated_heartbeat=""),
        Fact(general_pain=""),
        Fact(swelling_eye=""),
        Fact(itchy_eye=""),
        Fact(burning_eye=""),
        Fact(tearing_eye=""),
        Fact(redness_eye=""),
        Fact(involuntary_weight_loss=""),
        Fact(irritability=""),
        Fact(weakness=""),
        Fact(hand_numbness=""),
        Fact(sleep_problems=""),
        Fact(poor_apetite=""),
        Fact(burning_sensation=""),
        Fact(shudder=""),
        Fact(sensitivity_to_light=""),
        Fact(sound_sensitivity=""),
        Fact(hyperactivity=""),
        Fact(neck_stifness=""),
        Fact(facial_pressure=""),
        Fact(stomach_cramps=""),
        Fact(blood_in_stool=""),
    )
    def disease_8(self):
        self.declare(Fact(disease="Hiatal-hernia"))
        
    # Disease 9 - Migraine

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion=""),
        Fact(diarrhea=""),
        Fact(abdominal_pain=""),
        Fact(muscular_pain=""),
        Fact(low_sense_of_taste=""),
        Fact(low_sense_of_smell=""),
        Fact(breathing_difficulties=""),
        Fact(accelerated_heartbeat=""),
        Fact(general_pain=""),
        Fact(swelling_eye=""),
        Fact(itchy_eye=""),
        Fact(burning_eye=""),
        Fact(tearing_eye=""),
        Fact(redness_eye=""),
        Fact(involuntary_weight_loss=""),
        Fact(irritability=""),
        Fact(weakness=""),
        Fact(hand_numbness=""),
        Fact(sleep_problems=""),
        Fact(poor_apetite=""),
        Fact(burning_sensation=""),
        Fact(shudder=""),
        Fact(sensitivity_to_light=""),
        Fact(sound_sensitivity=""),
        Fact(hyperactivity=""),
        Fact(neck_stifness=""),
        Fact(facial_pressure=""),
        Fact(stomach_cramps=""),
        Fact(blood_in_stool=""),
    )
    def disease_9(self):
        self.declare(Fact(disease="Migraine"))
        
    # Disease 10 - Rhinosinusitis

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion=""),
        Fact(diarrhea=""),
        Fact(abdominal_pain=""),
        Fact(muscular_pain=""),
        Fact(low_sense_of_taste=""),
        Fact(low_sense_of_smell=""),
        Fact(breathing_difficulties=""),
        Fact(accelerated_heartbeat=""),
        Fact(general_pain=""),
        Fact(swelling_eye=""),
        Fact(itchy_eye=""),
        Fact(burning_eye=""),
        Fact(tearing_eye=""),
        Fact(redness_eye=""),
        Fact(involuntary_weight_loss=""),
        Fact(irritability=""),
        Fact(weakness=""),
        Fact(hand_numbness=""),
        Fact(sleep_problems=""),
        Fact(poor_apetite=""),
        Fact(burning_sensation=""),
        Fact(shudder=""),
        Fact(sensitivity_to_light=""),
        Fact(sound_sensitivity=""),
        Fact(hyperactivity=""),
        Fact(neck_stifness=""),
        Fact(facial_pressure=""),
        Fact(stomach_cramps=""),
        Fact(blood_in_stool=""),
    )
    def disease_10(self):
        self.declare(Fact(disease="Rhinosinusitis"))
        
    # Disease 11 - Salmonellosis 

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion=""),
        Fact(diarrhea=""),
        Fact(abdominal_pain=""),
        Fact(muscular_pain=""),
        Fact(low_sense_of_taste=""),
        Fact(low_sense_of_smell=""),
        Fact(breathing_difficulties=""),
        Fact(accelerated_heartbeat=""),
        Fact(general_pain=""),
        Fact(swelling_eye=""),
        Fact(itchy_eye=""),
        Fact(burning_eye=""),
        Fact(tearing_eye=""),
        Fact(redness_eye=""),
        Fact(involuntary_weight_loss=""),
        Fact(irritability=""),
        Fact(weakness=""),
        Fact(hand_numbness=""),
        Fact(sleep_problems=""),
        Fact(poor_apetite=""),
        Fact(burning_sensation=""),
        Fact(shudder=""),
        Fact(sensitivity_to_light=""),
        Fact(sound_sensitivity=""),
        Fact(hyperactivity=""),
        Fact(neck_stifness=""),
        Fact(facial_pressure=""),
        Fact(stomach_cramps=""),
        Fact(blood_in_stool=""),
    )
    def disease_11(self):
        self.declare(Fact(disease="Salmonellosis"))
        
    # Disease 12 - Tuberculosis

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(chills="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(fatigue="no"),
        Fact(sunken_eyes="no"),
        Fact(vomiting="no"),
        Fact(restlessness="low"),
        Fact(sore_throat="no"),
        Fact(fever="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
        Fact(nasal_congestion=""),
        Fact(diarrhea=""),
        Fact(abdominal_pain=""),
        Fact(muscular_pain=""),
        Fact(low_sense_of_taste=""),
        Fact(low_sense_of_smell=""),
        Fact(breathing_difficulties=""),
        Fact(accelerated_heartbeat=""),
        Fact(general_pain=""),
        Fact(swelling_eye=""),
        Fact(itchy_eye=""),
        Fact(burning_eye=""),
        Fact(tearing_eye=""),
        Fact(redness_eye=""),
        Fact(involuntary_weight_loss=""),
        Fact(irritability=""),
        Fact(weakness=""),
        Fact(hand_numbness=""),
        Fact(sleep_problems=""),
        Fact(poor_apetite=""),
        Fact(burning_sensation=""),
        Fact(shudder=""),
        Fact(sensitivity_to_light=""),
        Fact(sound_sensitivity=""),
        Fact(hyperactivity=""),
        Fact(neck_stifness=""),
        Fact(facial_pressure=""),
        Fact(stomach_cramps=""),
        Fact(blood_in_stool=""),
    )
    def disease_12(self):
        self.declare(Fact(disease="Tuberculosis"))

    #when the user's input doesn't match any disease in the knowledge base
    @Rule(Fact(action="find_disease"), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = self.get_details(id_disease)
        print("")
        print("Your symptoms match %s\n" % (id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details + "\n")

    @Rule(
        Fact(action="find_disease"),
        Fact(headache=MATCH.headache),
        Fact(chills=MATCH.chills),
        Fact(chest_pain=MATCH.chest_pain),
        Fact(cough=MATCH.cough),
        Fact(sore_throat=MATCH.fainting),
        Fact(fatigue=MATCH.fatigue),
        Fact(sunken_eyes=MATCH.sunken_eyes),
        Fact(vomiting=MATCH.vomiting),
        Fact(restlessness=MATCH.restlessness),
        Fact(sore_throat=MATCH.sore_throat),
        Fact(fever=MATCH.fever),
        Fact(nausea=MATCH.nausea),
        Fact(blurred_vision=MATCH.blurred_vision),
        Fact(nasal_congestion=MATCH.nasal_congestion),
        Fact(diarrhea=MATCH.diarrhea),
        Fact(abdominal_pain=MATCH.abdominal_pain),
        Fact(muscular_pain=MATCH.muscular_pain),
        Fact(low_sense_of_taste=MATCH.low_sense_of_taste),
        Fact(low_sense_of_smell=MATCH.low_sense_of_smell),
        Fact(breathing_difficulties=MATCH.breathing_difficulties),
        Fact(accelerated_heartbeat=MATCH.accelerated_heartbeat),
        Fact(general_pain=MATCH.general_pain),
        Fact(swelling_eye=MATCH.swelling_eye),
        Fact(itchy_eye=MATCH.itchy_eye),
        Fact(burning_eye=MATCH.burning_eye),
        Fact(tearing_eye=MATCH.tearing_eye),
        Fact(redness_eye=MATCH.redness_eye),
        Fact(involuntary_weight_loss=MATCH.involuntary_weight_loss),
        Fact(irritability=MATCH.irritability),
        Fact(weakness=MATCH.weakness),
        Fact(hand_numbness=MATCH.hand_numbness),
        Fact(sleep_problems=MATCH.sleep_problems),
        Fact(poor_apetite=MATCH.poor_apetite),
        Fact(burning_sensation=MATCH.burning_sensation),
        Fact(sensitivity_to_light=MATCH.sensitivity_to_light),
        Fact(sound_sensitivity=MATCH.sound_sensitivity),
        Fact(hyperactivity=MATCH.hyperactivity),
        Fact(neck_stifness=MATCH.neck_stifness),
        Fact(facial_pressure=MATCH.facial_pressure),
        Fact(stomach_cramps=MATCH.stomach_cramps),
        Fact(blood_in_stool=MATCH.blood_in_stool),
        NOT(Fact(disease=MATCH.disease)),
        salience=-999
    )
    def not_matched(
        self,
        headache,
        chills,
        chest_pain,
        cough,
        fainting,
        fatigue,
        sunken_eyes,
        vomiting,
        restlessness,
        sore_throat,
        fever,
        nausea,
        blurred_vision,
        nasal_congestion,
        diarrhea,
        abdominal_pain,
        muscular_pain, 
        low_sense_of_taste,
        low_sense_of_smell,
        breathing_difficulties,
        accelerated_hearbeat,
        general_pain,
        swelling_eye, 
        itchy_eye,
        burning_eye,
        tearing_eye,
        redness_eye, 
        involuntary_weight_loss,
        irritability,
        weakness,
        hand_numbness,
        sleep_problems,
        poor_apetite,
        burning_sensation,
        sensitivy_to_light,
        sound_sensitivity,
        hyperactivity,
        neck_stifness,
        facial_pressure,
        stomach_cramps,
        blood_in_stool
    ):
        print("\nThe bot did not find any diseases that match your exact symptoms.")
        lis = [
            headache,
            chills,
            chest_pain,
            cough,
            fainting,
            fatigue,
            sunken_eyes,
            vomiting,
            restlessness,
            sore_throat,
            fever,
            nausea,
            blurred_vision,
            nasal_congestion,
            diarrhea,
            abdominal_pain,
            muscular_pain, 
            low_sense_of_taste,
            low_sense_of_smell,
            breathing_difficulties,
            accelerated_hearbeat,
            general_pain,
            swelling_eye, 
            itchy_eye,
            burning_eye,
            tearing_eye,
            redness_eye, 
            involuntary_weight_loss,
            irritability,
            weakness,
            hand_numbness,
            sleep_problems,
            poor_apetite,
            burning_sensation,
            sensitivy_to_light,
            sound_sensitivity,
            hyperactivity,
            neck_stifness,
            facial_pressure,
            stomach_cramps,
            blood_in_stool
        ]
        max_count = 0
        max_disease = ""
        for key, val in self.symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and (lis[j] == "high" or lis[j] == "low" or lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if max_disease != "":
            self.if_not_matched(max_disease)