import os
import random

def generate_plots(total_space, min_plot_size, max_plot_size, plots_directory='plots'):
    remaining_space = total_space
    plots = []
    
    if not os.path.exists(plots_directory):
        os.makedirs(plots_directory)

    while remaining_space > 0:
        # Preferowane proporcje rozmiaru działki
        preferred_ratio = 0.8

        # Dostępny zakres rozmiarów działek
        current_plot_size = max(min_plot_size, min(max_plot_size, int(remaining_space * preferred_ratio)))

        # Tworzymy nową działkę
        plot_position = random.randint(0, total_space - current_plot_size)
        plot_data = (plot_position, current_plot_size)
        plots.append(plot_data)

        # Zapisz dane działki na dysk
        save_plot_data(plots_directory, plot_data)

        # Aktualizuj pozostałą przestrzeń dyskową
        remaining_space -= current_plot_size
    
    return plots

def save_plot_data(directory, plot_data):
    plot_number = len(os.listdir(directory)) + 1
    plot_filename = f"plot_{plot_number}.dat"
    plot_path = os.path.join(directory, plot_filename)

    # Tutaj możesz zapisywać rzeczywiste dane działki na dysk
    # Na razie tworzymy jedynie pusty plik o odpowiednim rozmiarze
    with open(plot_path, 'wb') as plot_file:
        plot_file.write(b'\0' * plot_data[1])

# Przykładowe użycie
total_disk_space = 4096000000  # 4096 MB pamięci
min_plot_size = 4000000  # Min. rozmiar jednej działki (MB)
max_plot_size = 128000000  # Max. rozmiar jednej działki (MB)
plots_directory = 'plots/'

plots = generate_plots(total_disk_space, min_plot_size, max_plot_size, plots_directory=plots_directory)

# Wyświetlamy wyniki
for i, plot in enumerate(plots, 1):
    print(f"Plot {i}: Position {plot[0]}, Size {plot[1]} MB")
