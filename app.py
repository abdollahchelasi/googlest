import pywhatkit
import streamlit as st


st.set_page_config(page_title="گوگل قشمی" ,page_icon="g.png")

with open('c.css') as f:
    st.markdown(f"<style> {f.read()} </style>",unsafe_allow_html=True)

st.image("g.png",width=200)
ser = st.text_input("گوگل قشمی")


if st.button("جستجوی گوگل قشمی"):
    
    pywhatkit.search(ser)
    
st.divider()
st.markdown("[ساخته شده توسط عبدالله چلاسی](https://abdollahchelasi.streamlit.app)")
    



    
# pywhatkit.sendwhatmsg("+98", "سلام کانال ترفندون رو دنبال بکن ", 15, 3)



# # ارسال یک عکس به گروه با کپشن
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")
#
# # ارسال عکس به مخاطب بدون کپشن
# pywhatkit.sendwhats_image("+98", "Images/Hello.png")
#
# #ارسال پیام به گروه در ساعت 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)
#
# # ارسال پیام فوری به گروه
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
#
# # پخش ویدیو در یوتیوب
# pywhatkit.playonyt("PyWhatKit")
#

    
# #این دستور در گوگل سرچ میکند




#
# #این دستور اطلاعات در مورد هر تاپیکی به شما میدهد
# pywhatkit.info('' , 3)
#
# # این دستور نوشته را به دستخط تبدیل میکند
# pywhatkit.text_to_handwriting('' , 'pywhatkit.png')
