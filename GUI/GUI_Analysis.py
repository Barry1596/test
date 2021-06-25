from scipy.fft import fft, fftfreq
import numpy as np
from GUI import GUI_Config

#Define Fast Fourier Transform from to convert time domain into frequency domain
def FFT_Vibrometer(data):
    
    #Number of sample point
    N = len(data)
    
    #Define Spacing
    T = 1.0/N
    
    #Define Time 
    time = np.linspace(0.0, N*T, N, endpoint=False)
    
    #Define Acc
    Acc = data
    
    #Perform FFT with scipy
    Acc_f = fft(Acc)
    Freq = fftfreq(N, T)[:N//2]
    
    #Plot_FFT
    FFT_X_plot = Freq
    FFT_Y_Plot = 2.0/N * np.abs(Acc_f[0:N//2])
    max_Amp = max(FFT_Y_Plot)
    
    #Accesing natural frequency value
    for i in range(len(FFT_Y_Plot)):
        if FFT_Y_Plot[i] == max(FFT_Y_Plot):
            nat_freq = FFT_X_plot[i]
    
    return[FFT_X_plot, FFT_Y_Plot, max_Amp, nat_freq]

#Define Bridge Condition Rating
def Bridge_Condition_Rating(nat_freq):
    
    #Define The change of natural frequency
    delta_f = abs(GUI_Config.INITIAL_NATURAL_FREQUENCY-nat_freq)/GUI_Config.INITIAL_NATURAL_FREQUENCY
    
    #Calculate Bridge Condition rating of the bridge based on change natural frequency
    G = delta_f*1000/123
    BCR = int(9-G)
    
    #Define Alert that define based on value of BCR
    if BCR == 9 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'EXELLENT CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = 'EXELLENT CONDITION'
    elif BCR == 8 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'VERY GOOD CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = 'No problems noted'
    elif BCR == 7 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'GOOD CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = 'Some minor problems'
    elif BCR == 6 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'SATISFACTORY CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = 'Structural elements show some minor deterioration'
    elif BCR == 5 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'FAIR CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = 'Primary structural elements are sound but may have some minor section loss, cracking, spalling or scour'
    elif BCR == 4 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'POOR CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = 'Advanced section loss, deterioration, spalling or scour'
    elif BCR == 3 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'SERIOUS CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = 'Loss of section, deterioration spalling or scour have seriously affected primary structural components. Local failure are possible. Fatigue crack in steel or shear cracks in concrete may be present'
    elif BCR == 2 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'CRITICAL CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = ' Advanced deterioration of primary structural elements. Fatigue crack in steel or shear cracks in concrete may be present or scour may have removed substructure support. Unless closely monitored, the bridge may have to be dosed until corrective action is taken'
    elif BCR == 1 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'IMMINENT FAILURE CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = 'Major deterioration or section loss present in critical structural components or obvious vertical or horizontal movement affecting structure stability. Bridge is closed to trafic but corrective action may pur back in light service'
    elif BCR == 0 :
        GUI_Config.ALERT['Bridge_Condition_Rating'] = 'FAILED CONDITION'
        GUI_Config.ALERT['Bridge_Desc_Condition'] = 'Out of service - beyond corrective action'
    return(BCR)

#Define Bridge Load Rating
def Bridge_Load_Rating(max_Amp, nat_freq, deflection):
    
    #Calculate The Effective EI
    EI = (nat_freq^2)*(np.pi^2)*(GUI_Config.BRIDGE_SPAN^3)*GUI_Config.TOTAL_MASS_BRIDGE/59.68 
    
    #Calculate Stiffness (K)
    K = 768*EI/(7*((GUI_Config.BRIDGE_SPAN)^3))
    
    #Calculate DLFA (Dynamic Load Factor Acceleration)
    DLFA = max_Amp / GUI_Config.INITIAL_PEAK_AMPLITUDE
    if DLFA < 1.33 :
        DLFA = 1.33
    elif DLFA > 1.33 :
        DLFA = DLFA
    
    #Calculate Bridge Capacity
    Static_Bridge_Capacity = K*deflection/(DLFA*2000)
    
    #Calculate Load Rating
    BLR = Static_Bridge_Capacity/GUI_Config.WEIGHT_LIVE_LOAD
    
    #Define Alert Based on value of BLR
    if BLR > 1 :
        GUI_Config.ALERT['Bridge_Load_Rating'] = 'The structure is ADEQUATE static capacity'
    elif BLR < 1:
        GUI_Config.ALERT['Bridge_Load_Rating'] = 'The structure is UNADEQUATE static capacity or not safe'
    return(BLR)

#Define Deflection Limit of the bridge   
def Bridge_Deflection_Limit(deflection):
    
    #Calculate Limit in mm
    Limit = GUI_Config.BRIDGE_SPAN * 1000 / 800 
    
    #ALERT
    if deflection > Limit :
        GUI_Config.ALERT['Bridge_Deflection_Limit'] = 'The deflection is OVER CAPACITY'
    elif deflection < Limit :
        GUI_Config.ALERT['Bridge_Deflection_Limit'] = 'The deflection is STILL ACCEPTABLE'
    
    
    
    

    
    
    
        
    
                            
                            
    

