import utils
from matplotlib import pyplot as plt

# TODO: Find a way to target both belts at the same speed also
# TODO: Fix the header names


def main():
    data_folder = "data"
    project_name = "pilot"
    session_name = "session01"
    trial_name = "trial01"
    data_path = utils.construct_data_path(data_folder, project_name, session_name, trial_name)

    # Read the data
    data = utils.read_csv(data_path)

    # Plot the data
    t = data.Time - data.Time[0]
    # Plot force in the vertical direction
    plt.figure()
    plt.title("Force in the vertical direction")
    plt.plot(t, data.FP1ForceY)
    plt.plot(t, data.FP2ForceY)
    plt.xlabel("Time (s)")
    plt.ylabel("Force (N)")
    plt.legend(["FP1", "FP2"])

    # Plot the Belts speed and target speed
    plt.figure()
    plt.title("Belts speed and target speed")
    plt.plot(t, data.LeftBelt, color="tab:blue")
    plt.plot(t, data.RightBelt, color="tab:orange")
    plt.plot(t, data.LeftBeltTarget, color="tab:blue", linestyle="--")
    plt.plot(t, data.RightBeltTarget, color="tab:orange", linestyle="--")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (m/s)")
    plt.legend(["Left belt", "Right belt", "Left belt target", "Right belt target"])

    plt.show()


if __name__ == "__main__":
    main()
