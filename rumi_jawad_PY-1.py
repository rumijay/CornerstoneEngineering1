# Program: Amino Acid Molecular Weight Calculator
# Rumi Jawad
# Date: September 24, 2026
# Version: 1

# Store the atomic masses needed for the calculations
carbon = 12.011

# Store the atomic mass of hydrogen
hydrogen = 1.008

# Store the atomic mass of nitrogen
nitrogen = 14.007

# Store the atomic mass of oxygen
oxygen = 15.999

# Store the atomic mass of sulfur
sulfur = 32.06

# Display a message introducing the calculator
print("Amino Acid Molecular Weight Calculator")

# Ask the user to enter  name of the amino acid
amino_acid = input("Enter the name of the amino acid: ")

# Ask how many carbon atoms are in the amino acid
carbon_atoms = int(input("Enter the number of carbon atoms: "))

# Ask how many hydrogen atoms are in the amino acid
hydrogen_atoms = int(input("Enter the number of hydrogen atoms: "))

# Ask how many nitrogen atoms are in the amino acid
nitrogen_atoms = int(input("Enter the number of nitrogen atoms: "))

# Ask how many oxygen atoms are in the amino acid
oxygen_atoms = int(input("Enter the number of oxygen atoms: "))

# Ask how many sulfur atoms are in the amino acid
sulfur_atoms = int(input("Enter the number of sulfur atoms: "))

# Calculate the contribution of carbon to the molecular weight
carbon_weight = carbon * carbon_atoms

# Calculate the contribution of hydrogen to the molecular weight
hydrogen_weight = hydrogen * hydrogen_atoms

# Calculate the contribution of nitrogen to the molecular weight
nitrogen_weight = nitrogen * nitrogen_atoms

# Calculate the contribution of oxygen to the molecular weight
oxygen_weight = oxygen * oxygen_atoms

# Calculate the contribution of sulfur to the molecular weight
sulfur_weight = sulfur * sulfur_atoms

# Add the atomic contributions to find the molecular weight
molecular_weight = carbon_weight + hydrogen_weight + nitrogen_weight + oxygen_weight + sulfur_weight

# Add all atom quantities to fnd3 the total number of atoms
total_atoms = carbon_atoms + hydrogen_atoms + nitrogen_atoms + oxygen_atoms + sulfur_atoms

# Divide the molecular weight by the number of atoms
average_weight = molecular_weight / total_atoms

# Display the amino acid entered by theuser
print("Amino acid:", amino_acid)

# Display the calculated moleclar weight with three decimal places
print("Molecular weight: {:.3f}".format(molecular_weight))

# Display the total number of atoms
print("Total number of atoms:", total_atoms)

# Display the average atomic weight with three decimal places
print("Average weight per atom: {:.3f}".format(average_weight))