from django.db import models
# Create your models here.


# The Employee Table


class employee (models.model):

    SEX=(
        ("M"="male"),
        ("F"="Female")
    )

    Fname=models.CharField(max_length=250)
    Minit=CharField(max_length=1)
    Lname=CharField(max_length=250)
    ssn=models.BigAutoField(primary_key=True)
    adress=models.CharField(max_length=350)
    bdate=DateField()
    salary=models.IntegerField(max_length=200)
    Dno=models.ForeignKey(Department,on_delete=models.CASCADE)

            #Another Try:-
    
    #sex=models.CharField("sex",max_length=1,choices=SEX)
    
    sex= models.CharField(max_length=9, choices=SEX, default='M')
    super_ssn=models.ForeignKey(empolyee,on_delete=models.CASCADE)

    #Another TRY

# ** super_ssn = models.OneToOneField(empolyee, on_delete=models.CASCADE,primary_key=False,)

  class Department (models.model):
    Dname=models.CharField(max_length=200)
    Dnumber=models.IntegerField(max_length=2,primary_key=True)
    Mgr_ssn=BigAutoField(primary_key=False)
     Mgr_stratdate=models.DateField()

      # The Department Table

     class Dept_locations (models.model):

       Dnumber=models.ForeignKey(Department,primary_key=True, on_delete=models.CASCADE)
      Dlocation=models.CharField(max_length=400, primary_key=True)
      
      # The Project Table 

      class Project (models.model):
        Pname=models.CharField(max_length=200)
        Pnumber=models.IntegerField(max_length=2, primary_key=True)
        Plocation=models.CharField(max_length=200)
        Dnum=models.ForeignKey(Department,on_delete=models.CASCADE)

  
      # Works ON Table

      class Works_On (modes.model):
      Essn=models.ForeignKey(employee,primary_key=True, on_delete=models.CASCADE)
      Pno=models.ForeignKey(Project,primary_key=True, on_delete=models.CASCADE)
      Hours=models.FloatFeild=()


      # Dependent Table 

      class Dependent (models.model):
        essn=models.ForeignKey(employee,primary_key=True,on_delete=models.CASCADE)
        Dependent_name=models.CharField(max_length=200,primary_key=True)
        sex2=models.CharField(max_length=9, choices=SEX, default='M') 
        Bdate=models.DateField()


        # Relationships Tupels

        Relationships= (
          
            ("Daughter)"=("Daughter"),
            ("Son")=("Son"),
            ("Daughter")=("Daughter"),
            ("Spouse")=("Spouse"),
            ("Spouse")=("Spouse"),
            ("Son")=("Son"),
            ("Spouse")=("Spouse"),

                       ) 

            relationship= models.CharField(max_length=9, choices=Relationships, default='Son')



