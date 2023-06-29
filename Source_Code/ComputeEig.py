def create_mesh_1D(xmin, xmax, nx):
    # Create a 1D mesh with uniform element size
    # Input:
    #   xmin: minimum x coordinate
    #   xmax: maximum x coordinate
    #   nx: number of elements
    # Output:
    #   mesh: dictionary containing the mesh data (elements, nodes, etc.)
    mesh = {}
    mesh['nelements'] = nx
    mesh['nnodes'] = nx+1
    mesh['nodes'] = np.linspace(xmin, xmax, nx+1)
    mesh['elements'] = np.vstack((np.arange(nx), np.arange(1, nx+1))).T
    return mesh

def apply_boundary_conditions_1D(A, bc):
    # Apply boundary conditions to the global stiffness matrix for a 1D finite element problem.
    # Input:
    #   A: global stiffness matrix
    #   bc: boundary condition vector (0: unknown, 1: Dirichlet, 2: Neumann)
    # Output:
    #   A: modified global stiffness matrix

    # Get the number of nodes
    nnodes = A.shape[0]

    # Loop over the nodes
    for i in range(nnodes):
        if bc[i] == 1:
            # Dirichlet boundary condition: set the row and column to zero, except for the diagonal element
            A[i, :] = 0
            A[:, i] = 0
            A[i, i] = 1
        elif bc[i] == 2:
            # Neumann boundary condition: set the diagonal element to zero
            A[i, i] = 0

    return A

def compute_element_matrices_1D(mesh, e, D, r):
    # Compute the element mass and stiffness matrices for a 1D finite element problem
    # using the linearized elliptic operator of the Fisher-Kolmogorov equation.
    # Input:
    #   mesh: dictionary containing the mesh data (elements, nodes, etc.)
    #   e: index of the element
    #   D: diffusivity
    #   r: growth rate
    # Output:
    #   me: element mass matrix
    #   ke: element stiffness matrix

    # Extract the nodes of the element
    nodes = mesh['elements'][e, :]

    # Compute the element length
    h = mesh['nodes'][nodes[1]] - mesh['nodes'][nodes[0]]

    # Compute the element mass matrix
    me = me = np.array([[1/3, 1/6], [1/6, 1/3]]) * h[:, np.newaxis]

    # Compute the element stiffness matrix
    ke = np.array([[1, -1], [-1, 1]]) * (D / h[:, np.newaxis])

    return me, ke

def assemble_FE_matrices_1D(mesh, D, r):
    # Assemble the mass and stiffness matrices for a 1D finite element problem
    # using the linearized elliptic operator of the Fisher-Kolmogorov equation.
    # Input:
    #   mesh: dictionary containing the mesh data (elements, nodes, etc.)
    #   D: diffusivity
    #   r: growth rate
    # Output:
    #   M: mass matrix
    #   K: stiffness matrix
    M = np.zeros((mesh['nnodes'], mesh['nnodes']))
    K = np.zeros((mesh['nnodes'], mesh['nnodes']))

    # Loop over the elements
    for e in range(mesh['nelements']):
        # Extract the nodes of the element
        nodes = mesh['elements'][e, :]

        # Compute the element mass and stiffness matrices
        me, ke = compute_element_matrices_1D(mesh, e, D, r)

        # Assemble the element matrices into the global matrices
        M[nodes, nodes] = M[nodes, nodes] + me
        K[nodes, nodes] = K[nodes, nodes] + ke

    return M, K

import numpy as np

# Define the domain and mesh size
xmin = 0
xmax = 1
nx = 10

# Create a mesh
mesh = create_mesh_1D(xmin, xmax, nx)

# Define the diffusivity D and growth rate r
D = 1
r = 2

# Define the finite element matrices
M, K = assemble_FE_matrices_1D(mesh, D, r)

# Assemble the global stiffness matrix
A = K + M

# Define the boundary conditions
bc = np.zeros(nx+1)
bc[0] = 1
bc[nx] = 1

# Apply the boundary conditions
A = apply_boundary_conditions_1D(A, bc)

# Solve for the eigenvalues and eigenvectors of the global stiffness matrix
w, V = np.linalg.eig(A)

# Sort the eigenvalues in ascending order
idx = w.argsort()
w = w[idx]

# Print the eigenvalues to the console
print(w)