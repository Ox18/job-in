export const timeAgo = (date) => {
  const listedDate = new Date(date);
  const currentDate = new Date();
  const timeDifference = currentDate - listedDate; // Diferencia en milisegundos
  const daysDifference = Math.floor(timeDifference / (1000 * 60 * 60 * 24)); // Convertir a días

  if (daysDifference === 0) {
    return "Hoy";
  } else if (daysDifference === 1) {
    return "Hace 1 día";
  } else {
    return `Hace ${daysDifference} días`;
  }
};
