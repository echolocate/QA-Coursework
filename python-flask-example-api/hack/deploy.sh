#! /bin/sh

service_user='flask-app'
service_name='flask-app'
install_directory="/opt/${service_name}"

main() {
    check_user_is_root
    create_service_user
    install_application_files
    install_pip_dependencies
    install_systemd_unit
}

check_user_is_root() {
    if [ "$(id -u)" -ne "0" ]; then
        echo "You need to be root to run this script:"
        echo "\n\tsudo ./hack/deploy.sh\n"
        exit 1
    fi
}

create_service_user() {
    if ! cat /etc/passwd | awk -F: '{ print $1 }' | grep -w "${service_user}" > /dev/null; then
        sudo useradd --system --no-create-home --shell /bin/false ${service_user}
    fi
}

install_application_files() {
    rm -rf ${install_directory}
    mkdir ${install_directory}
    cp app.py requirements.txt ${install_directory}
}

install_pip_dependencies() {
    cd ${install_directory}
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    cd -
}

install_systemd_unit() {
    cp ${service_name}.service /etc/systemd/system/${service_name}.service
    systemctl daemon-reload
    systemctl restart ${service_name}
}

main

