### Java vs. Python ###

# class structure

# Java
# public class Dog {
#   private String name;
#   private int age;
#   public Dog (String name, int age) {
#       this.name = name;
#       this.age = age;
#   }
#   public int getAge() {
#       return age;
#   }
#   public String getName() {
#       return name;
#   }
#   public void setAge(int a) {
#       age = a;
#   }
#   public void setName(String n) {
#       name = n;
#   }
#   public String toString() {
#       return "Dog:\nName: " + name + "\nAge: " + age;
#   }
#   public static void main(String[] args) {
#       Dog d1 = new Dog("Carly", 10);
#       System.out.println(d1);
#   }
# }

# Python
# class name does NOT have to be the same name as the module/file
# self makes the method an instance method, without makes it a class method
# just like Java's static operator
class Dog:
    def __init__(self, name, age):
        # underscore in front of the period means that the variable is private
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def random():
        return 7

    def __str__(self):
        return "Dog:\nName: " + self._name + "\nAge: " + str(self._age)

d1 = Dog("Scruffy", 5)
print(d1)
print(d1.get_age())
print(Dog.random())
