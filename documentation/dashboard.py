import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'C:\Users\WhaZz\Documents\ESGI\4IABD\AWS\AWS-Project\data\goodreads_train_from_RDS.csv', sep=',')
dataset.columns = ['nbLines', 'user_id', 'book_id', 'review_id', 'rating', 'review_text', 'date_added', 'date_updated', 'read_at', 'started_at', 'n_votes', 'n_comments']

# ? Create the Variables for the charts

    # ? Variables for the bar chart
values_for_class = dataset.groupby(by=["rating"]).count()
values_for_class = values_for_class['nbLines']
values_for_class = values_for_class.to_frame()
values_for_class = values_for_class.rename(columns={"0": "nbLines"})
values_for_class = values_for_class.sort_values(by=['rating'])
class_possible = [0,1,2,3,4,5]
values_for_class = values_for_class.reindex(class_possible)

    # ? Variables for the pie chart
pie_dataset = dataset.groupby(by=["user_id"]).count().reset_index()
pie_count = pie_dataset['nbLines']	
pie_user = pie_dataset['user_id']
pie_dataset = pd.concat([pie_count, pie_user], axis=1)

tab_line= []
for element in pie_dataset['nbLines']:
    tab_line.append(element)

tab_user = []
for element in pie_dataset['user_id']:
    tab_user.append(element)

labels = list(tab_user)

    # ? Variables for the 2nd pie chart

pie_2 = dataset.sort_values(by=['n_comments'], ascending=False).reset_index()
pie_count = pie_2['n_comments']
pie_book = pie_2['book_id']	
pie_grade = pie_2['rating']
pie_2 = pd.concat([pie_count, pie_book, pie_grade], axis=1)

tab_percent = []
tab_infos = []
percent = pie_2['n_comments'].sum()

for element in range(0, 10):
    tab_percent.append(round((pie_2['n_comments'][element]/percent)*100, 2))
    infos = str(pie_2['book_id'][element]) + ' (' + str(pie_2['n_comments'][element]) + ' coms - ' + str(pie_2['rating'][element]) + '*)'
    tab_infos.append(infos)

labels_2= list(tab_infos)

# ? End of the Variables for the charts



# ? Create the report

image = Image.open(r'C:\Users\WhaZz\Documents\ESGI\4IABD\AWS\AWS-Project\documentation\src\Logo-RDS.png')
st.image(image)

st.title(':orange[AWS] Project - Integration of data in the Amazon Cloud')


st.header('Step 1 : Structured Data')

st.markdown('> Made with Amazon RDS and Python')

col1, col2, col3 = st.columns(3)
col1.metric("Rows in Dataset", dataset.shape[0], "100")
col2.metric("Classes in Dataset", "6")
col3.metric("F1 Score", "60,010%", "1,023%")

st.subheader('Data Table')

st.markdown("> Below, you can see the data table analyzed during this reporting")

st.dataframe(dataset)

st.subheader('Distribution of scores given by users')
st.bar_chart(values_for_class['nbLines'])


st.subheader('Distribution of contributions by user')

st.markdown("> According to our dataset : Some users have contributed much more than others. The opinions will therefore be less representative of a given population.")

fig1, pie_chart = plt.subplots()
pie_chart = plt.pie(tab_line, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'color':"w"}, colors=['#E19451', '#DC7F2E'])
fig1.patch.set_facecolor('#0E1117')
st.pyplot(fig1)


st.subheader('Distribution of the number of comments per book (Top 10)')

st.markdown("> From our dataset : The books with the most reviews are often the ones with the highest ratings.")

fig2, pie_chart_2 = plt.subplots()
pie_chart_2 = plt.pie(tab_percent, labels=labels_2, autopct='%1.1f%%', startangle=90, textprops={'color':"w"}, colors=['#3C5B7C', '#42658A', '#496F97', '#5079A5', '#5A83AF', '#688DB6', '#7597BD', '#83A1C3', '#91ABCA', '#9FB5D1'])
fig2.patch.set_facecolor('#0E1117')
st.pyplot(fig2)



st.markdown('## __Step 2 : Unstructured Data__')

st.markdown('> Made with a bucket Amazon S3 and AWS CLI')

col4, col5, col6 = st.columns(3)
col4.metric("Element in the Bucket", "11")
col5.metric("Classes in the Bucket", "2")
col6.metric("Type of data", "Pictures")

st.markdown("> The bucket contains images that have been manipulated in our Deep Learning course. The goal was to create modifications on images using python script.")

y = np.array([4, 7])
mylabels = ["Filtered", "Original"]

fig3, pie_chart_3 = plt.subplots()
pie_chart_3 = plt.pie(y, labels = mylabels, startangle = 90, textprops={'color':"w"},  autopct='%1.1f%%')
fig3.patch.set_facecolor('#0E1117')
fig3.set_size_inches(2,2)
st.pyplot(fig3)
