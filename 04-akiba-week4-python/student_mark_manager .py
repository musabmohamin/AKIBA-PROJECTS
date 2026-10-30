
marks = [75, 80, 65, 90, 85]

shared_marks = marks

copied_marks = marks.copy()

copied_marks.append(95)

print("Original marks:", marks)
print("Shared reference:", shared_marks)
print("Copied marks:", copied_marks)

print()

print("Original and shared reference are identical:", marks is shared_marks)
print("Original and copied lists have equal values:", marks == copied_marks)
print("Original and copied lists are identical:", marks is copied_marks)
