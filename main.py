import customtkinter as ctk
import numpy as np

# Function to perform matrix multiplication and display result
def solve_matrix():
    try:
        # Get matrix size
        n = int(matrix_size_entry.get())
        
        # Create empty matrices for A, B, and X
        A = np.zeros((n, n))
        B = np.zeros((n, 1))
        
        # Get values from matrix A entries
        for i in range(n):
            for j in range(n):
                try:
                    A[i][j] = float(A_entries[i][j].get())
                except ValueError:
                    raise ValueError(f"Invalid input in A[{i+1}][{j+1}]")
        
        # Get values from matrix B entries
        for i in range(n):
            try:
                B[i][0] = float(B_entries[i].get())
            except ValueError:
                raise ValueError(f"Invalid input in B[{i+1}]")
        
        # Check if the matrix A is singular (determinant is zero)
        if np.linalg.det(A) == 0:
            raise np.linalg.LinAlgError("Singular Matrix: No unique solution")
        
        # Solve for X (X = A^-1 * B)
        X = np.linalg.solve(A, B)
        
        # Display result in the result labels
        for i in range(n):
            result_labels[i].configure(text=f"X[{i+1}] = {X[i][0]:.2f}")
        
    except ValueError as e:
        # Show error if inputs are invalid
        for i in range(n):
            result_labels[i].configure(text=f"Error: {str(e)}")
    except np.linalg.LinAlgError as e:
        # Handle case where A is singular (non-invertible)
        for i in range(n):
            result_labels[i].configure(text=f"Error: {str(e)}")

# Function to clear all fields
def clear_display():
    matrix_size_entry.delete(0, ctk.END)
    for row in A_entries:
        for entry in row:
            entry.delete(0, ctk.END)
    for entry in B_entries:
        entry.delete(0, ctk.END)
    for label in result_labels:
        label.configure(text="")

# Function to generate matrix input fields based on size
def generate_matrices():
    try:
        # Get the matrix size
        n = int(matrix_size_entry.get())
        
        # Create matrix A input fields dynamically
        global A_entries
        A_entries = []
        for i in range(n):
            row_entries = []
            for j in range(n):
                entry = ctk.CTkEntry(root, width=50, height=30, font=("Arial", 14), justify="center")
                entry.grid(row=i+2, column=j, padx=5, pady=5)
                row_entries.append(entry)
            A_entries.append(row_entries)
        
        # Create matrix B input fields
        global B_entries
        B_entries = []
        for i in range(n):
            entry = ctk.CTkEntry(root, width=50, height=30, font=("Arial", 14), justify="center")
            entry.grid(row=i+2, column=n+1, padx=5, pady=5)
            B_entries.append(entry)
        
        # Create result labels for displaying X
        global result_labels
        result_labels = []
        for i in range(n):
            label = ctk.CTkLabel(root, text="", font=("Arial", 14), width=120)
            label.grid(row=i+2, column=n+2, padx=10, pady=5)
            result_labels.append(label)
        
        # Create Solve and Clear buttons
        solve_button = ctk.CTkButton(root, text="Solve Matrix", font=("Arial", 14), command=solve_matrix, width=15)
        solve_button.grid(row=n+2, column=0, columnspan=3, padx=10, pady=10)
        
        clear_button = ctk.CTkButton(root, text="Clear", font=("Arial", 14), command=clear_display, width=15)
        clear_button.grid(row=n+3, column=0, columnspan=3, padx=10, pady=10)
        
    except ValueError:
        error_label = ctk.CTkLabel(root, text="Please enter a valid integer for N.", font=("Arial", 14))
        error_label.grid(row=1, column=0, columnspan=2, pady=5)

# Set up the main window
root = ctk.CTk()
root.title("Matrix Solver")
root.geometry("600x600")  # Set window size

# Add a title label
title_label = ctk.CTkLabel(root, text="Matrix Solver: Solve A * X = B", font=("Arial", 18), width=500)
title_label.grid(row=0, column=0, columnspan=3, pady=20)

# Create the input field for matrix size
ctk.CTkLabel(root, text="Enter Matrix Size (N):", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5)
matrix_size_entry = ctk.CTkEntry(root, width=60, font=("Arial", 14), justify="center")
matrix_size_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a button to generate matrix fields
generate_button = ctk.CTkButton(root, text="Generate Matrix", font=("Arial", 14), command=generate_matrices, width=15)
generate_button.grid(row=1, column=2, padx=10, pady=5)

# Run the Tkinter main loop
root.mainloop()
