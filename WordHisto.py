# WordHisto.py
from TPlot.TPlot import TPlot #import TPlot class for drawing
import string #for string punctuation in the text preprocessing
import math #for mathematical operations

#gloabl variable to store the TPlot instance
tp = None


def read_file(fname):
    """Reads a text file and returns a list of words."""
    try:
        #try to open and read the file
        with open(fname, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        #handle case where file doesn't exist
        print(f"Error: File '{fname}' not found.")
        return []

    #process the text and return list of words
    return preprocess_text(text)


def preprocess_text(text):
    """Removes punctuation and converts text to lowercase before splitting into words."""
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    #split text into words and return as list
    return text.split()


def count_word_lengths(words):
    """Returns a dictionary mapping word lengths to their frequency."""
    #initialise empty dictionary to store counts
    word_length_counts = {}

    #count frequency of each word length
    for word in words:
        length = len(word)
        if length in word_length_counts:
            #increment count if length already exists
            word_length_counts[length] += 1
        else:
            #initialise count if first word of this length
            word_length_counts[length] = 1
    return word_length_counts


def get_colour_for_bar(index, total_bars):
    """Returns a colour name based on the bar index."""
    # List of colours available in TkColours
    colours = ["green", "blue", "red", "orange", "purple", "cyan", "magenta"]
    #use module to go through different colours and cycle through colours if the number of bars is greater than the number of colours
    return colours[index % len(colours)]


def draw_axes(max_length, max_count):
    """Draws the x and y axes with labels."""
    global tp

    #pen set up for drawing
    tp.SetPenSize(2)
    tp.SetPenColour("black")

    # Draw x-axis and y-axis
    tp.DrawLine(0, 0, max_length * 15, 0)  # x-axis
    tp.DrawLine(0, 0, 0, max_count)  # y-axis - extend exactly to max_count

    # Add axis labels
    tp.WriteAt(max_length * 7.5, -max_count * 0.15, "Word Length")  # X-axis label
    tp.WriteAt(-50, max_count * 0.5, "Frequency")  # Y-axis label

    # Add title
    tp.WriteAt(max_length * 5, max_count * 1.1, "Word Length Histogram", ("Arial", 16, "bold"))

    # Draw y-axis scale
    draw_y_scale(max_count)

    # Draw x-axis scale
    draw_x_scale(max_length, max_count)


def draw_y_scale(max_count):
    """Draws the y-axis scale with increments of 10."""
    global tp

    #increments of 10 for the y-axis scale
    step_size = 10  # Fixed step size of 10
    num_steps = max_count // step_size  # Integer division
    if max_count % step_size != 0:  # If there's a remainder, add an extra step
        num_steps += 1


    for i in range(0, num_steps + 1):
        y_val = i * step_size
        # Draw tick mark
        tp.DrawLine(-1, y_val, 0, y_val)
        # Add label
        tp.WriteAt(-15, y_val - 3, str(y_val))


def draw_x_scale(max_length, max_count):
    """Draws the x-axis scale with labels for each word length."""
    global tp

    bar_spacing = 10  # Same spacing used for bars

    #draw labels for each position on x-axis
    for length in range(1, max_length + 1):
        x_pos = length * bar_spacing
        # Draw x-axis label
        tp.WriteAt(x_pos - 2, -10, str(length))


def draw_bars(word_length_counts, max_length):
    """Draws the histogram bars based on word length counts."""
    global tp

    # Bar width and spacing
    bar_width = 5 #half width of each bar
    bar_spacing = 10 #distance between bars
    colour_index = 0 #start with first colour in the list

    # Draw the bars using actual heights
    for length in range(1, max_length + 1):
        if length in word_length_counts:
            count = word_length_counts[length]

            # Calculate bar position
            x_pos = length * bar_spacing

            # Set a unique color for each bar
            bar_colour = get_colour_for_bar(colour_index, len(word_length_counts))
            tp.SetPenColour(bar_colour)

            # Draw filled bar
            for i in range(-bar_width, bar_width + 1):
                tp.DrawLine(x_pos + i, 0, x_pos + i, count)

            # Draw border around the bar
            tp.SetPenColour("black")
            tp.SetPenSize(1)

            # Draw the four sides of the bar
            left_x = x_pos - bar_width
            right_x = x_pos + bar_width
            top_y = count

            #draw three sides of the border
            tp.DrawLine(left_x, 0, left_x, top_y)  # Left side
            tp.DrawLine(right_x, 0, right_x, top_y)  # Right side
            tp.DrawLine(left_x, top_y, right_x, top_y)  # Top side

            # Add the count above each bar
            tp.SetPenColour("black")
            tp.WriteAt(x_pos - 5, top_y + 5, str(count))

            #move to next colour for next bar
            colour_index += 1


def draw_legend(max_length, max_count):
    """Draws the legend explaining the histogram."""
    global tp

    #position legend on the upper right of the chart
    legend_x = max_length * 8
    legend_y = max_count * 0.8

    tp.SetPenColour("black")
    tp.WriteAt(legend_x, legend_y + 10, "Legend:", ("Arial", 12, "bold"))
    tp.WriteAt(legend_x, legend_y, "Each bar represents frequency of")
    tp.WriteAt(legend_x, legend_y - 10, "words with given length")
    tp.WriteAt(legend_x, legend_y - 20, "X-axis: Word length in characters")
    tp.WriteAt(legend_x, legend_y - 30, "Y-axis: Number of occurrences")


def plot_histogram(word_length_counts):
    """Plots a histogram of word lengths using TPlot."""
    global tp

    # Initialise or clear the plotting area
    if tp is None:
        tp = TPlot()
    else:
        tp.Clear()

    # Find the max word length and count for better scaling
    all_word_lengths = []
    for length in word_length_counts.keys():
        all_word_lengths.append(length)

    max_length = max(all_word_lengths)
    if max_length < 16:
        max_length = 16

    #find max frequency count
    max_count = 0
    for count in word_length_counts.values():
        if count > max_count:
            max_count = count

    #handles empty data case
    if max_count == 0:
        max_count = 1

    # Round up max_count to nearest 10 for better scale increments
    max_count = (max_count // 10) * 10
    if max_count % 10 != 0:  # If there's a remainder, round up
        max_count += 10

    # Set ranges with proper spacing
    tp.SetRanges(-25, -20, max_length * 15, max_count * 1.3)

    # Draw the axes, scales, and labels
    draw_axes(max_length, max_count)

    # Draw the histogram bars
    draw_bars(word_length_counts, max_length)

    # Draw the legend
    draw_legend(max_length, max_count)

    # Update and show
    tp.Show()


def Histo(FName):
    """Main function to read file, process word lengths, and plot histogram."""
    words = read_file(FName)
    if not words:
        return #exit if file is empty or not found

    #count frequency of each word length
    word_length_counts = count_word_lengths(words)
    print("Word Length Counts:", word_length_counts)

    #create and display the histogram
    plot_histogram(word_length_counts)