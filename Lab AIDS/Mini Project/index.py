import streamlit as st
import pickle

with open('random_forest_classifier.pkl', 'rb') as file:
    clf = pickle.load(file)

def prediction(final_values):
    output = clf.predict([final_values])
    return output

def main():
    st.title('Passenger Satisfaction Prediction')

    slider_list = ['Inflight wifi service',
                'Departure/Arrival time convenient',
                'Ease of Online booking',
                'Gate location',
                'Food and drink',
                'Online boarding',
                'Seat comfort',
                'Inflight entertainment',
                'On-board service',
                'Leg room service',
                'Baggage handling',
                'Checkin service',
                'Inflight service',
                'Cleanliness']

    rating = [-1]*14

    col1, col2 = st.columns(2, gap='large')

    with col1:
        age = st.number_input('Age', min_value=0,max_value=120, value=0)
        gender = st.radio('Gender',options=['Male','Female'])
        for i in range(0,len(slider_list),2):
            rating [i] = st.slider(slider_list[i], min_value=0, max_value=5)
        departure_delay = st.number_input('Departure Delay(in Minutes)', min_value=0, value=0)
        travel_class = st.radio('Class',options=['Business','Economy', 'Economy Plus'])

    with col2:
        flight_distance = st.number_input('Flight Distance', min_value=0, value=0)
        cust_type = st.radio('Customer Type',options=['Loyal Customer','Disloyal Customer'])
        for i in range(1,len(slider_list),2):
            rating [i] = st.slider(slider_list[i], min_value=0, max_value=5)
        arrival_delay = st.number_input('Arrival Delay(in Minutes)', min_value=0, value=0)
        travel_type = st.radio('Type of Travel',options=['Business travel','Personal Travel'])

    if st.button('Predict'):
        final_values = []
        final_values += [age, flight_distance]
        final_values += rating
        final_values += [departure_delay, arrival_delay]

        if gender == 'Male':
            final_values += [0,1]
        else:
            final_values += [1,0]

        if cust_type == 'Loyal Customer':
            final_values += [1,0]
        else:
            final_values += [0,1]

        if travel_class == 'Business':
            final_values += [1,0,0]
        elif travel_class == 'Economy':
            final_values += [0,1,0]
        else:
            final_values += [0,0,1]

        if travel_type == 'Business travel':
            final_values += [1,0]
        else:
            final_values += [0,1]

        print(final_values)

        result = prediction(final_values)
        st.success('The output is {}.'.format(result[0]))

if __name__ == '__main__':
    main()
