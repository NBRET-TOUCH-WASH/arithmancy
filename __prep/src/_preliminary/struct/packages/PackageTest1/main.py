#coding:utf-8

#modules
import testPackage

uninteresting_shape = testPackage.geometry.shape.Shape("Octoriogon", 8**3)
print(uninteresting_shape)

uninteresting_rectangle = testPackage.geometry.rectangle.Rectangle(4, 20)
print(uninteresting_rectangle)
print("The rectangle's perimeter equals", uninteresting_rectangle.get_perimeter(), "units.")
print("The rectangle's surface area equals", uninteresting_rectangle.get_surface_area(), "units².")

uninteresting_square = testPackage.geometry.square.Square(666)
print(uninteresting_square)
print("The square's perimeter equals", uninteresting_square.get_perimeter(), "units.")
print("The square's surface area equals", uninteresting_square.get_surface_area(), "units².")