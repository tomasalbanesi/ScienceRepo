% Parámetros
frecuencia = 50;  % Frecuencia en Hz
amplitud = 230;   % Amplitud de la tensión en V
angulo = 0;       % Ángulo de fase en grados
periodos = 3;     % Número de periodos a graficar

% Generar tensiones trifásicas balanceadas
t = 0:1/10000:(1/frecuencia)*periodos;  % Vector de tiempo con tres periodos
voltageA = amplitud * sqrt(2) * sin(2 * pi * frecuencia * t + deg2rad(angulo));
voltageB = amplitud * sqrt(2) * sin(2 * pi * frecuencia * t + deg2rad(angulo - 120));
voltageC = amplitud * sqrt(2) * sin(2 * pi * frecuencia * t + deg2rad(angulo + 120));

% Plotear las tensiones en un solo gráfico
figure(1);
plot(t, voltageA, 'r', 'linewidth', 1.5)
hold on;
plot(t, voltageB, 'g', 'linewidth', 1.5)
plot(t, voltageC, 'b', 'linewidth', 1.5)
% Resaltar la línea horizontal del eje y en negrita
line([t(1), t(end)], [0, 0], 'Color', 'k', 'LineWidth', 1);
hold off;
title('Tensiones Trifásicas');
xlabel('Tiempo (s)');
ylabel('Tensión (V)');
legend('Fase R', 'Fase S', 'Fase T');
grid on;
axis tight;
