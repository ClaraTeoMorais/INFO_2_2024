import streamlit as st

class Eq_2grau:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def __str__(self):
        return (f"{self.a}x² + {self.b}x + {self.c}")
    
    def delta(self):
        return (self.b**2 - 4 * self.a * self.c)
    
    def tem_raizes_reais(self):
        if Eq_2grau.delta() < 0:
            return False
        else:
            return True
    
    def raiz1(self):
        
        return print((-self.b + (Eq_2grau.delta()**1/2)) / 2 * self.a)
    
    def raiz2(self):
        return print((-self.b - (Eq_2grau.delta()**1/2)) / 2 * self.a)
    
class UI:
    st.header("CÁLCULO DE EQUAÇÃO DO SEGUNDO GRAU")
    a = st.text_input("a")
    b = st.text_input("b")
    c = st.text_input("c")

    if st.button("Calcular"):
        eq = Eq_2grau(a, b, c)
        st.write(eq)
        st.write(f"Delta = {eq.delta()}")
        st.write(f"X1 = {eq.raiz1()}")
        st.write(f"X2 = {eq.raiz2()}")
