import streamlit as st
import Brain as Brain
from streamlit_option_menu import option_menu


st.set_page_config(page_title="PLAN-B", page_icon="/Users/omkarvyas/Documents/AI_Projects/AI_Recruit(M)/MicrosoftTeams-image.png")
def main():
    print('Main is working')
    
    st.markdown('## Travel Plan')
    
    
    with st.sidebar:
        selected = option_menu(
            menu_title = "Main Menu",
            options =["Show routes", "Go Plan"]
        )
         
    if selected == "Show routes":
        if not  st.session_state.get('started'):
          From = st.text_input('From')
          To = st.text_input('To')
          days = st.text_input('Number of days')     
    
   
    if 'key' not in st.session_state:
        st.session_state['key'] = Brain.greet()
    
    st.write(st.session_state['key'])

    if not  st.session_state.get('started'):
        
        From = st.text_input('From')
        To = st.text_input('To')
        days = st.text_input('Number of days')
        
        
        
        if st.button('Show Routes'):
            
                if 'route' not in st.session_state:
                  st.session_state['route'] = Brain.routes(From,To)
                
                st.session_state['started'] = True
                st.session_state['From'] = From
                st.session_state['To'] = To
                st.write(st.session_state['route'])
                
        if st.button('Go plan'):
            
            if 'plan' not in st.session_state:
             st.session_state['plan'] = Brain.plan(From,To,days)
            
            st.write(st.session_state['plan'])
       
        
        

if __name__ == '__main__':
    print('code started')
    main()
    
