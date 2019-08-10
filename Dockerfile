FROM ubuntu:latest
ARG PYVER
RUN apt-get update
RUN export DEBIAN_FRONTEND=noninteractive && apt-get install -y python3-pip python3-pyside python3-opencv -
RUN export DEBIAN_FRONTEND=noninteractive && apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev -y 
RUN export DEBIAN_FRONTEND=noninteractive && apt-get install git-core -y

# Create code directory
RUN mkdir /src

RUN apt-get install -y python3-dev python-dev

# Create user
ENV HOME /home/pyinstaller
ENV PYENV_ROOT "$HOME/.pyenv"
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
# ENV CC clang
# ENV PYTHON_CONFIGURE_OPTS "--enable-framework"
RUN useradd -m pyinstaller
RUN chown pyinstaller:pyinstaller /src
RUN chmod 775 /src
WORKDIR ${HOME}
USER pyinstaller

# PyEnv install
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
ENV PYTHON_CONFIGURE_OPTS "--enable-shared"
RUN pyenv install ${PYVER}
RUN pyenv global ${PYVER}
RUN pyenv rehash
RUN eval "$(pyenv init -)" >> ~/.bashrc && exec $SHELL
RUN pip install --upgrade pip
RUN pip install pyinstaller

VOLUME /src/
WORKDIR /src

CMD ["sh"]

# rm -rf dist; docker run --rm -v "$(pwd):/src/" cdrx/pyinstaller-linux "apt-get update -y && apt-get install -y wget python3.7 python3-pip python3-pyside python3-opencv && pip install -r requirements.txt && pyinstaller --clean -y --dist ./dist/linux --workpath /tmp *.spec"

# pyinstaller --clean -y --dist ./dist --workpath /tmp --onefile actionreplay.py

# docker build --build-arg PYVER=3.7.4 -t test . && docker run --rm -it -v "$(pwd)/actionreplay_app:/src/" test

# docker build --build-arg PYVER=3.7.4 -t cemt1990/pyinstaller:latest -t cemt/pyinstaller:0.3 .
# docker run --rm -v "$(pwd)/actionreplay_app:/src/" cemt/pyinstaller:latest sh "pip install -r requirements.txt && pyinstaller --clean -y --dist ./dist --workpath /tmp --onefile actionreplay.py"