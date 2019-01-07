package org.apache.ignite.ml.util;

import org.jetbrains.annotations.Nullable;

public class NullTMPLogger implements TMPLogger {

    @Override public TMPLogger getLogger(Object ctgr) {
        return null;
    }

    @Override public void trace(String msg) {

    }

    @Override public void debug(String msg) {

    }

    @Override public void info(String msg) {

    }

    @Override public void warning(String msg, @Nullable Throwable e) {

    }

    @Override public void error(String msg, @Nullable Throwable e) {

    }

    @Override public boolean isTraceEnabled() {
        return false;
    }

    @Override public boolean isDebugEnabled() {
        return false;
    }

    @Override public boolean isInfoEnabled() {
        return false;
    }

    @Override public boolean isQuiet() {
        return false;
    }

    @Override public String fileName() {
        return null;
    }
}
