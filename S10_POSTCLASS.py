import streamlit as st
co1,co2 = st.columns(2)
toppinglist=['Trân châu trắng (5K)','Trân châu đen (5K)','Thạch rau câu (6K)','Vải (7K)','Nhãn (8K)','Đào (10K)']
toppingprice=[5,5,6,7,8,10]
with co1:
    st.title('Trà Sữa CoTAI')
    st.image('https://i.imgur.com/lEpdPsT.jpeg')
    topping=st.multiselect('Topping',toppinglist)
with co2:
    size=st.radio('Kích cỡ',('Nhỏ (30K)', 'Vừa (40K)', 'Lớn (50K)'),horizontal=True)
    st.text('Thêm')
    co3,co4=st.columns(2)
    with co3:
        milk=st.checkbox ('Sữa (5K)')
        coffee= st.checkbox('Cà phê (8K)')
    with co4:
        cream=st.checkbox('Kem (10K')
        egg=st.checkbox('Trứng (15K)')
    quant=st.number_input('Số lượng',value=0)
note=st.text_input('Ghi chú')
cost=0
if st.button ('Đặt hàng',use_container_width=True):
    # size
    if size=='Nhỏ (30K)':
        st.write('Cỡ nhỏ')
        cost=30
    elif size == 'Vừa (40K)':
        st.write('Cỡ vừa')
        cost=40
    elif size== 'Lớn (50K)':
        st.write('Cỡ lớn')
        cost=50
    # add
    if milk==True:
        if coffee==True:
            if cream == True:
                if egg==True:
                    st.write('Thêm: Sữa, Cà phê, Kem, Trứng')
                    cost=cost+5+8+10+15
                else:
                    st.write('Thêm: Sữa, Cà phê, Kem')
                    cost=cost+5+8+10
            else:
                st.write('Thêm: Sữa, Cà phê')
                cost=cost+5+8
        else:
            st.write('Thêm: Sữa')
            cost=cost+5
    else:
        st.write('Thêm: Không có')
    # topping
    st.write('Topping:',*topping)
    st.write(note)
    st.write('Số lượng:',quant)
    # cost
    for i in range (len(toppinglist)):
        if toppinglist[i] in topping:
            cost+=toppingprice[i]
    cost*=quant
    st.write('Thành tiền:',str(cost)+'K')