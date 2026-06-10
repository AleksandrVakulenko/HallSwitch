% NOTE: 
% Test script N2
% Check single relay command
%


%% include 'aDevice'

Fern.load('aDevice')

%%


clc

COM_port = 3;

Box = Hall_box(COM_port);

CMD = "ABCD";

try
    disp('Set relay:')
    [err_status, err_no, err_comment] = Box.set_relay(CMD);
    if err_status
        disp(['ERROR ' num2str(err_no) ': '])
        disp(err_comment)
    else
        disp('No errors')
    end

catch err
    delete(Box);
    warning([newline 'Device is closed in error section'])
    rethrow(err);
end


delete(Box)
disp([newline 'Device is closed'])

