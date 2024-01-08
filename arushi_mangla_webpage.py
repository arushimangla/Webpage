#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install streamlit_option_menu


# In[7]:


import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image
import base64

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Arushi Mangla ", page_icon=":woman_tipping_hand:")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# # ---- LOAD ASSETS ----
img_profile = Image.open("IMG_7314.jpg")
with open("Arushi Mangla Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# -----Title----
st.write('''<div style = "text-align: center"> <b>“Torture the data, and it will confess to anything.”</b> – <i>By Ronald Coase</i> </div><br>''',
            unsafe_allow_html=True
            )
# -----Option menu----

selected = option_menu(None, ["About me", "Resume", "Contact me"],
    icons=['file-person', 'file-earmark', 'envelope-open'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
           "container": {"padding": "0!important"},
           "icon": {"font-size": "16px"},
           "nav-link": {"font-size": "16px", "text-align": "left", "margin": "10px"}
           }
                       )


if selected == "About me":

    with st.container():
        img_column, right_column = st.columns(2)
        with img_column:
            st.markdown('''
            ''')
            st.image(img_profile,
                     width = 300
                     )
        with right_column:
            st.markdown('''
                        ## Hi there 👋, I am Arushi
                        <p style = "text-align: jusitfied">
                                                
                        #### ML and Python Developer
                        
                        Hey, I'm Arushi Mangla, a dedicated Machine Learning enthusiast currently pursuing my Masters at Santa Clara University. An avid reader & passionate traveler who believes in seizing opportunities & experimenting with my skills as much as I can. With almost 3 years of experience in the field of Data Science & Business Analytics, I have always believed that the more you pitch your data, the more it'll speak. Let's innovate and make an impact together! 🚀 #DataScience #SCUGradStudent**CARPE DIEM**
                        </p>
                        
                        #### **WHAT I DO**
                          - 🔭 I’m currently working as Graduate Research Assistant
                          - 💻 I’m currently learning Large Language Models and Vector Databases
                          - ☕ I’m looking to collaborate on projects based on Data Science and Machine Learning
                          - 🧗‍♀️ Over weekends, I like traveling to unchartered territories both in real life or behind the screens, and love challenging myself for new adventures on every forefront. Learning for me thus never stops, whether it be in upskilling my technical knowledge or understanding how to scale 15,000 ft mountains.

                       
                        ''',
                        unsafe_allow_html = True
                        )



if selected == "Resume":
    with st.container():
    # ---Download---
        st.download_button(label="Download",
                           data=PDFbyte,
                           file_name="Arushi Mangla Resume.pdf",
                           mime='application/octet-stream'
                           )

    #Name
        st.markdown('''
        # <div style = "text-align: center">Arushi Mangla</div>''',
                    unsafe_allow_html=True
        )
    #links
        st.markdown(
            """ <p style = "text-align: center">
                <a style = "text-align: center">San Francisco Bay Area, USA</a> <span>&nbsp;</span> | <span>&nbsp;</span>
                <a style='text-align: center;' href="https://www.linkedin.com/in/arushi-mangla-325099134/">LinkedIn</a> <span>&nbsp;</span> | <span>&nbsp;</span>
                                <a style='text-align: center;' href="+1 (669) 292-6446">+1 (669) 292-6446</a> <span>&nbsp;</span> | <span>&nbsp;</span>
                <a style='text-align: center;' href="amangla@scu.edu">amangla@scu.edu</a>
                </p>
            """,
            unsafe_allow_html=True,
        )
    #Education
        st.markdown(
            """ 
            ### Education 
             **Santa Clara University**, **Santa Clara, California** <br>
             Masters of Science in Computer Science and Engineering<br> June 2025
            * Areas Of Interest: Machine Learning, Computer Vision, Data Science, Research  
            **Computer Skills:** Python, MySQL, Google Cloud Platform, Microsoft Power BI,
                        Large Langauge Models, Generative AI, Tensorflow, Numpy, Pandas, 
                        Basic OpenCV, Scikit-Learn, Matplotlib.                 
            """,
            unsafe_allow_html=True,
        )

    # WORK EX
        st.markdown(
            '''
            ### Work Experience
            **Honasa Consumer Limited** <br>
            *System Analyst* <br>
            *10/2020 - 07/2023*
            
              * Created data pipelines using API calls in Python & automated more than 40% of daily manual reporting using interactive dashboards, mailers & KPI trackers.
              * Leveraged Python to analyze extensive datasets, identifying key patterns and trends in marketing campaigns, ultimately driving a 12% sales increase through data-backed recommendations for customer acquisition strategies.
              * Improved the payment success rate by 10% by building real-time alerting systems & deep diving on failure points through data exploration.
              * Used Power BI, SQL & Excel Macros to build reports on customer retention through different channels; visualized KPIs for expected sales, conversion and churn.
                        
            
            **Mu Sigma** <br>
            *Data Scientist* <br>
            *08/2020 - 10/2020*
                    
              * Analyzed transactional behavior, constructed 10+ hypotheses, developed data dictionaries, and created strategic roadmaps for 'The Home Depot,' leading to a 15% boost in in-store customer satisfaction.
            
            **KPMG** <br>
            *Data Analytics Intern*<br> 
            *06/2020 - 06/2020*
              
              * Performed comprehensive data quality assessments on a dataset of 10,000+ records, yielding 98% accuracy, and extracted actionable insights that led to a 15% improvement in decision-making processes.
                        
            **GLA University** <br>
            *Research Team Lead*<br> 
            *05/2019 - 07/2020*
                        
              * Co-authored 7 research papers with undergrad students and university professors in the field of STEM.
              * Mentored students with their research work and technical writing in areas such as Machine Learning, Artificial Intelligence, Cyber Security & Big Data.
              * Conducted workshops for paper presentation & draft formation, along with guiding teams on how to work in different domain areas.
             
            **GIBots** <br>
            *Data Science Intern*<br> 
            *05/2019 - 07/2019*
                        
              * Led a results-oriented collaboration on a project aimed at achieving multilingual handwritten text recognition using OCR (Tesseract OCR 4.0 with LSTM), resulting in a 20% improvement in text recognition accuracy across various languages.Led a results-oriented collaboration on a project aimed at achieving multilingual handwritten text recognition using OCR (Tesseract OCR 4.0 with LSTM), resulting in a 20% improvement in text recognition accuracy across various languages. 
            ''',
            unsafe_allow_html =True
        )

    # Projects
        st.markdown(
            '''
            ### PROJECTS                      
            **Fine-tuning GenAI Models** <br>
              * Fine-tuned large language models from the hugging face repository using an evaluative dataset containing sentiments and reviews for domain specific results.
            
            **Sentiment Analysis using BERT**<br>
              * Led a sentiment analysis project utilizing the IMDb dataset of 50,000 reviews, emphasizing the transformative impact of employing BERT transformers. Through advanced natural language processing techniques, including Bag of Words, n-grams, and NLTK, the project achieved a 90% accuracy.
            ''',
            unsafe_allow_html = True
        )

        
    # Patent
        st.markdown(
            '''
            ### PATENT                      
            **A Machine Learning based Brain Computer Interface system for training and enabling aphonic patient for effective communication** <br>
              * Intellectual Property India (IPI)
            ''',
            unsafe_allow_html = True
        )

    # Publication:
        st.markdown(
            '''
            ### PUBLICATIONS
            **Match-Level Fusion of Finger-Knuckle Print and Iris for Human Identity Validation Using Neuro-Fuzzy Classifier**<br>
             * International Journal of Quality & Reliability Management, Jul 2022*<br>
             
            **Operating of a Drone Using Human Intent Recognition and Characteristics of an EEG Signal**<br>
             *Institute of Electrical and Electronics Engineers (IEEE), Jan 2021*<br>
             
            **Promotion Response Modelling in Healthcare Analytics**<br>
             *International Conference on Recent Engineering and Technology (ICRET), Jun 2020*<br>
             
            **Secure Encryption Mechanism for Mental Health Data**<br>
             *TEST Engineering and Management, May 2020*<br>
             
            **Collaborative Functioning for Underwater Acoustic Sensor Communication using AURP (AUV-Assisted Underwater Routing Protocol)**<br>
             *Social Science Research Network (SSRN), Mar 2020*<br>
             
            **Enhancing Image Diagnosis by the Implementation of Transfer Classifiers**<br>
             *International Journal of Recent Technology and Engineering (IJRTE), Sep 2019*<br>
             
            **Encoded Data Methodologies for Cloud Computing Realm's Security Enhancement**<br>
             *International Journal of Recent Technology and Engineering (IJRTE), May 2019*<br>
            ''',
            unsafe_allow_html=True
        )

    # Professional Association
        st.markdown(
            '''
            ### PROFESSIONAL ASSOCIATION
            **Society of Women Engineers** <br>
            *Grad Representative* <br>
            *11/2023 - Present*
    
              * Helping newcomers into the field of Machine Learning as a Mentor.
              * Also contributing to the community of SWE as a hardworking Machine Learning Executive, working on projects based on ML/DL.
    
    
            **GLA University** <br>
            *Big Data Instructor* <br>
            *06/2020 - 08/2020*
    
              * Designing, delivering and presenting a complete big data coursework for University students.
              * Uplifting the students with new skills and making them learn new technologies.  
           '''
            , unsafe_allow_html=True
        )
    # SKILLS and INTERESTS:
        st.markdown(
            '''
            ### AWARDS & CERTIFICATIONS
            * Data Science Graduate by IBM, May 2020
            * Machine Learning & Deep Learning Specialization (5 Courses) by IIT Delhi, Udemy
            * Secured 1st and 2nd Prizes in Science Exhibitions

            
            ''',
            unsafe_allow_html = True
        )

    # ----Contact me----
if selected == "Contact me":
    with st.container():
        st.header("Get In Touch With Me!")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/amangla@scu.edu" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()


# In[ ]:




