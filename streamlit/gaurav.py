import streamlit as st
 
#BMI calculation funtion
def calculate_bmi(weight, height):
    if height !=0:
        height_m = height / 100 #convert height from cm to meters
        bmi = weight / (height_m**2)
        return bmi
    else:
        return 0

#Streamlit app
def main():
    st.title("BMI calculator")

    #user input
    weight =st.number_input("enter your weight(in kg)")
    height =st.number_input("enter your height(in cm)")

    #calculate BMI
    bmi =calculate_bmi(weight, height)

    #display result
    st.subheader("BMI result")
    st.write("Weight:",weight,"kg")
    st.write("Height:",height,"cm")

if bmi !=0:
    st.write("BMI"),bmi
else:
    st.write("plese enter a non_zero height value.")

    #BMI catagories
st.subheader("BMI catagories")
st.write("underweight:BMI<18.5")
st.write("normal weight:18.5<=BMI<24.9")
st.write("overweight:25<=BMI<29.9")
st.write("obesity:BMI>=30")

if __name__=="__main__":
    main()

