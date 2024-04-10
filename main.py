import utils
from matplotlib import pyplot as plt


def main():
    data_folder = "data"
    project_name = "pilot"
    session_name = "session01"
    trial_name = "Belts0014"
    data_path = utils.construct_data_path(data_folder, project_name, session_name, trial_name)

    # Read the data
    data = utils.read_csv(data_path)

    # Plot the data
    t = data.Time - data.Time[0]
    # Plot force in the vertical direction
    plt.figure()
    plt.title("Force in the vertical direction")
    plt.plot(t, data.FP1_ForceY)
    plt.plot(t, data.FP2_ForceY)
    plt.xlabel("Time (s)")
    plt.ylabel("Force (N)")
    plt.legend(["FP1", "FP2"])

    # Plot the Belts speed and target speed
    plt.figure()
    plt.title("Belts speed and target speed")
    plt.plot(t, data.LeftBelt_Speed, color="tab:blue")
    plt.plot(t, data.RightBelt_Speed, color="tab:orange")
    plt.plot(t, data.LeftBelt_TargetSpeed, color="tab:blue", linestyle="--")
    plt.plot(t, data.RightBelt_TargetSpeed, color="tab:orange", linestyle="--")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (m/s)")
    plt.legend(["Left belt", "Right belt", "Left belt target", "Right belt target"])

    plt.show()


if __name__ == "__main__":
    main()
