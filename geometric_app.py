import streamlit as st

st.set_page_config(page_title ="Squares and Triangles")

if __name__ == "__main__":
    class triangle:

        def __init__(self,base='lower side',height='vertical line with right angle',side1='side1',side2='side2',side3='side3',
                     opp = 'opposite to angle sigma',adj = 'adjacent to the angle sigma', hypo = 'the long side'):
            
            self.base = base
            self.height = height
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
            self.opp = opp
            self.adj = adj
            self.hypo = hypo
            
        def area(self):
            self.area = (self.base*self.height)/2
            return self.area


        def per(self):
            self.per = self.side1 + self.side2 + self.side3
            return self.per
        
        def sine(self):
            self.sine = (self.opp/self.hypo)
            return self.sine
        
        def cosine(self):
            self.cosine = (self.adj/self.hypo)
            return self.cosine
        
        def tangent(self):
            self.tangent= (self.opp/self.adj)
            return self.tangent

    class squares:
        def __init__(self,side):
            self.side = side
            
        def area(self):
            self.area = (self.side)**2
            return self.area
        
        def per(self):
            self.per = 4*(self.side)
            return self.per
        
        def diags(self):
            self.diags = (self.side) * 2** 0.5
            return self.diags

    t = st.selectbox("Choose a Geometric Shape",["Triangle","Square","Right Triangle (Trigonometry)"])
    st.write("")

    if t == "Triangle":

        rad = st.radio("Choose",["Area","Perimeter"])
        if rad == "Area":
            a= st.number_input("Type in base",value=0.0)
            b= st.number_input("Type in area",value=0.0)
            c = triangle(float(a),float(b))
            st.write("The Area is: ",c.area())


        if rad == "Perimeter":
            a= st.number_input("Type in 1st side",value=0.0)
            b= st.number_input("Type in 2nd side",value=0.0)
            c= st.number_input("Type in 3rd side",value=0.0)
            d=triangle(side1=float(a),side2=float(b),side3=float(c))
            st.write("The Perimeter is: ",d.per())

    elif t == "Square":

        rad = st.radio("Choose",["Area","Perimeter","Diagonal"])

        if rad == "Area":
            a= st.number_input("Type in side",value=0.0)
            c = squares(float(a))
            st.write("The Area is: ",c.area())


        if rad == "Perimeter":
            a= st.number_input("Type in side",value=0.0)
            c = squares(float(a))
            st.write("The Perimeter is: ",c.per())
            
        if rad == "Diagonal":
            a= st.number_input("Type in side",value=0.0)
            c = squares(float(a))
            st.write("The Diagonal is: ",c.diags())

    elif t == "Right Triangle (Trigonometry)":

        rad = st.radio("Choose",["Sin(θ)","Cos(θ)","Tan(θ)"])

        if rad == "Sin(θ)":
            a= st.number_input("Type in Opposite",value=1.0)
            b= st.number_input("Type in Hypotenuse",value=1.0)
            c = triangle(opp=float(a),hypo=float(b))
            st.write("Sin(θ) is: ",c.sine())


        if rad == "Cos(θ)":
            a= st.number_input("Type in Adjacent",value=1.0)
            b= st.number_input("Type in Hypotenuse",value=1.0)
            c = triangle(adj=float(a),hypo=float(b))
            st.write("Cos(θ) is: ",c.cosine())
            
        if rad == "Tan(θ)":
            a= st.number_input("Type in Opposite",value=1.0)
            b= st.number_input("Type in Adjacent",value=1.0)
            c = triangle(opp=float(a),adj=float(b))
            st.write("Tan(θ) is: ",c.tangent())       
