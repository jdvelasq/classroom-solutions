#
# docker build --tag=jdvelasq/grader:agd .
# docker push jdvelasq/grader:agd
# docker run --rm -v "$PWD":/datalake  --name grader jdvelasq/grader:agd
#
FROM jdvelasq/python:3.6.9-minimal

WORKDIR /app
COPY . /app

ENV DEBIAN_FRONTEND noninteractive

RUN pip3 install pyyaml

# Java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $PATH:$JAVA_HOME/bin
RUN apt-get update \
    && apt-get install -yq --no-install-recommends openjdk-8-jdk \
    && rm -rf /var/lib/apt/lists/*

# Hadoop
ENV HDP_VERSION 2.8.5
ENV PATH $PATH:/usr/local/hadoop/bin:/usr/local/hadoop/sbin
ENV HADOOP_CLASSPATH  /usr/lib/jvm/java-8-openjdk-amd64/lib/tools.jar
ENV HADOOP_HOME  /usr/local/hadoop
ENV HADOOP_CONF_DIR  /usr/local/hadoop/etc/hadoop
ENV HADOOP_COMMON_LIB_NATIVE_DIR  /usr/local/hadoop/lib/native
ENV HADOOP_OPTS  "-Djava.library.path=/usr/local/hadoop/lib/native"
ENV HADOOP_ROOT_LOGGER  "ERROR,console"

RUN curl -O https://www-eu.apache.org/dist/hadoop/common/hadoop-${HDP_VERSION}/hadoop-${HDP_VERSION}.tar.gz \
    && tar -xzf hadoop-${HDP_VERSION}.tar.gz \
    && mv hadoop-${HDP_VERSION} /usr/local/hadoop \
    && rm hadoop-${HDP_VERSION}.tar.gz \
    && chmod 0777 /usr/local/hadoop \ 
    && rm -rf /var/lib/apt/lists/* \
    && mv hadoop/conf/* /usr/local/hadoop/etc/hadoop/ \
    && mv hadoop/bin/* /usr/local/bin/ 
#    && mv etc/environment /etc/environment

# Pig
ENV PIG_VERSION 0.17.0
ENV PIG_HOME  /usr/local/pig
ENV PATH $PATH:/usr/local/pig/bin
RUN curl -O https://www-eu.apache.org/dist/pig/pig-$PIG_VERSION/pig-$PIG_VERSION.tar.gz \
    && tar -xzf pig-$PIG_VERSION.tar.gz \
    && mv pig-$PIG_VERSION /usr/local/pig \
    && mv pig/conf/* /usr/local/pig/conf/ \
    && rm pig-$PIG_VERSION.tar.gz \
    && rm -rf /var/lib/apt/lists/*

# Hive
ENV HIVE_VERSION 2.3.6
ENV HIVE_HOME  /usr/local/hive
ENV HIVE_CONF_DIR  /usr/local/hive/conf
ENV PATH $PATH:/usr/local/hive/bin        
RUN curl -O https://www-eu.apache.org/dist/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz \
    && tar -xzf apache-hive-$HIVE_VERSION-bin.tar.gz \
    && mv apache-hive-$HIVE_VERSION-bin /usr/local/hive \
    && rm apache-hive-$HIVE_VERSION-bin.tar.gz \
    && mv hive/conf/hive-site.xml  /usr/local/hive/conf/ \
    && mv hive/bin/* /usr/local/bin/ 

# Parte generica
EXPOSE 50070 8088 8888 5000
RUN rm -rf /app/*
ENV DEBIAN_FRONTEND= 
VOLUME /datalake
WORKDIR /datalake
ENTRYPOINT bash hive-start.sh && python3 grade.py