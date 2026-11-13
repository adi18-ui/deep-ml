import numpy as np

def distillation_loss(
    student_logits: np.ndarray,
    teacher_logits: np.ndarray,
    temperature: float = 1.0
) -> float:

    # Temperature-scaled logits
    student_scaled = student_logits / temperature
    teacher_scaled = teacher_logits / temperature

    # Subtract maximum for numerical stability
    student_scaled = student_scaled - np.max(student_scaled)
    teacher_scaled = teacher_scaled - np.max(teacher_scaled)

    # Softmax
    student_expo = np.exp(student_scaled)
    student_soft = student_expo / np.sum(student_expo)

    teacher_expo = np.exp(teacher_scaled)
    teacher_soft = teacher_expo / np.sum(teacher_expo)

    # Prevent log(0)
    epsilon = 1e-12
    student_soft = np.clip(student_soft, epsilon, 1.0)
    teacher_soft = np.clip(teacher_soft, epsilon, 1.0)

    # KL(teacher || student)
    D_kl = np.sum(
        teacher_soft * np.log(teacher_soft / student_soft)
    )

    loss = (temperature ** 2) * D_kl

    return round(float(loss), 4)