import streamlit as st
import numpy as np

queue = []
enter_flag = True
index_of_queue = 0
main_url = None

if st.subheader('Create queue'):
    N = st.number_input('Enter the number of videos: ')
    N = round(N)
    for i in range(N):
        q_url = st.text_input(f'Enter the {i+1} url: ')
        if q_url:
            queue.append(q_url)
    enter_flag = False

if enter_flag == True:
    main_url = st.text_input('Enter the url of video: ')
    if main_url:
        st.video(main_url)
else:
    try:
        main_url = queue[0]
    except IndexError:
        pass
    video_place = st.video(main_url)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = st.columns(11)
    back = col1.button('⏪')
    next = col11.button('⏩')
    if back:
        if index_of_queue == 0:
            st.write('This is the first video')
        else:
            main_url = queue[index_of_queue - 1]
            index_of_queue -= 1
            video_place.video(main_url)
    if next:
        if index_of_queue == len(queue) - 1:
            st.write('This is the last video')
        else:
            main_url = queue[index_of_queue + 1]
            index_of_queue += 1
            video_place.video(main_url)
